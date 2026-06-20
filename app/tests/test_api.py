import json
from unittest.mock import patch

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.api.app import app

client = TestClient(app)

VALID_REQUEST = {
    "user_id": "test-user-123",
    "thread_id": "test-thread-abc",
    "destination": "Tokyo, Japan",
    "budget": 3000,
    "interests": ["food", "temples"],
    "user_query": "Plan a 5-day trip to Tokyo.",
}

MOCK_ITINERARY = "Day 1: Arrive in Tokyo. Day 2: Visit Senso-ji temple."


def make_sse_event(node_name: str, updates: dict) -> str:
    return f"data: {json.dumps({node_name: updates})}\n\n"


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

class TestHealthEndpoint:
    def test_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_returns_ok_status(self):
        response = client.get("/health")
        assert response.json() == {"status": "ok"}


# ---------------------------------------------------------------------------
# POST /travel/plan
# ---------------------------------------------------------------------------

class TestPlanEndpoint:
    def test_valid_request_returns_200(self):
        with patch("app.api.routes.travel.generate_trip", return_value=MOCK_ITINERARY):
            response = client.post("/travel/plan", json=VALID_REQUEST)
        assert response.status_code == 200

    def test_response_contains_itinerary_field(self):
        with patch("app.api.routes.travel.generate_trip", return_value=MOCK_ITINERARY):
            response = client.post("/travel/plan", json=VALID_REQUEST)
        assert "itinerary" in response.json()

    def test_itinerary_value_matches_service_output(self):
        with patch("app.api.routes.travel.generate_trip", return_value=MOCK_ITINERARY):
            response = client.post("/travel/plan", json=VALID_REQUEST)
        assert response.json()["itinerary"] == MOCK_ITINERARY

    def test_missing_destination_returns_422(self):
        payload = {k: v for k, v in VALID_REQUEST.items() if k != "destination"}
        response = client.post("/travel/plan", json=payload)
        assert response.status_code == 422

    def test_missing_user_id_returns_422(self):
        payload = {k: v for k, v in VALID_REQUEST.items() if k != "user_id"}
        response = client.post("/travel/plan", json=payload)
        assert response.status_code == 422

    def test_missing_thread_id_returns_422(self):
        payload = {k: v for k, v in VALID_REQUEST.items() if k != "thread_id"}
        response = client.post("/travel/plan", json=payload)
        assert response.status_code == 422

    def test_missing_interests_returns_422(self):
        payload = {k: v for k, v in VALID_REQUEST.items() if k != "interests"}
        response = client.post("/travel/plan", json=payload)
        assert response.status_code == 422

    def test_missing_user_query_returns_422(self):
        payload = {k: v for k, v in VALID_REQUEST.items() if k != "user_query"}
        response = client.post("/travel/plan", json=payload)
        assert response.status_code == 422

    def test_invalid_budget_type_returns_422(self):
        payload = {**VALID_REQUEST, "budget": "expensive"}
        response = client.post("/travel/plan", json=payload)
        assert response.status_code == 422

    def test_empty_request_body_returns_422(self):
        response = client.post("/travel/plan", json={})
        assert response.status_code == 422

    def test_service_error_returns_500(self):
        with patch(
            "app.api.routes.travel.generate_trip",
            side_effect=HTTPException(status_code=500, detail="LLM unavailable"),
        ):
            response = client.post("/travel/plan", json=VALID_REQUEST)
        assert response.status_code == 500


# ---------------------------------------------------------------------------
# POST /travel/plan/stream
# ---------------------------------------------------------------------------

class TestStreamEndpoint:
    def test_valid_request_returns_200(self):
        def mock_stream(_):
            yield make_sse_event("itinerary_agent", {"itinerary": MOCK_ITINERARY})

        with patch("app.api.routes.travel.stream_trip", side_effect=mock_stream):
            response = client.post("/travel/plan/stream", json=VALID_REQUEST)
        assert response.status_code == 200

    def test_response_has_event_stream_content_type(self):
        def mock_stream(_):
            yield make_sse_event("itinerary_agent", {"itinerary": MOCK_ITINERARY})

        with patch("app.api.routes.travel.stream_trip", side_effect=mock_stream):
            response = client.post("/travel/plan/stream", json=VALID_REQUEST)
        assert "text/event-stream" in response.headers["content-type"]

    def test_response_lines_use_sse_data_prefix(self):
        def mock_stream(_):
            yield make_sse_event("supervisor", {"next_agents": ["flight_agent"]})
            yield make_sse_event("itinerary_agent", {"itinerary": MOCK_ITINERARY})

        with patch("app.api.routes.travel.stream_trip", side_effect=mock_stream):
            response = client.post("/travel/plan/stream", json=VALID_REQUEST)

        data_lines = [l for l in response.text.splitlines() if l.startswith("data:")]
        assert len(data_lines) == 2

    def test_each_event_is_valid_json(self):
        def mock_stream(_):
            yield make_sse_event("flight_agent", {"flights": ["Flight A", "Flight B"]})
            yield make_sse_event("itinerary_agent", {"itinerary": MOCK_ITINERARY})

        with patch("app.api.routes.travel.stream_trip", side_effect=mock_stream):
            response = client.post("/travel/plan/stream", json=VALID_REQUEST)

        for line in response.text.splitlines():
            if line.startswith("data:"):
                parsed = json.loads(line[len("data:"):].strip())
                assert isinstance(parsed, dict)

    def test_itinerary_present_in_itinerary_agent_event(self):
        def mock_stream(_):
            yield make_sse_event("supervisor", {"next_agents": ["itinerary_agent"]})
            yield make_sse_event("itinerary_agent", {"itinerary": MOCK_ITINERARY})

        with patch("app.api.routes.travel.stream_trip", side_effect=mock_stream):
            response = client.post("/travel/plan/stream", json=VALID_REQUEST)

        itinerary = None
        for line in response.text.splitlines():
            if line.startswith("data:"):
                event = json.loads(line[len("data:"):].strip())
                if "itinerary_agent" in event:
                    itinerary = event["itinerary_agent"].get("itinerary")

        assert itinerary == MOCK_ITINERARY

    def test_multiple_agent_events_are_all_streamed(self):
        agent_events = [
            make_sse_event("load_memory", {"user_profile": {}}),
            make_sse_event("supervisor", {"next_agents": ["flight_agent"]}),
            make_sse_event("flight_agent", {"flights": ["Flight A"]}),
            make_sse_event("itinerary_agent", {"itinerary": MOCK_ITINERARY}),
        ]

        def mock_stream(_):
            yield from agent_events

        with patch("app.api.routes.travel.stream_trip", side_effect=mock_stream):
            response = client.post("/travel/plan/stream", json=VALID_REQUEST)

        data_lines = [l for l in response.text.splitlines() if l.startswith("data:")]
        assert len(data_lines) == len(agent_events)

    def test_missing_destination_returns_422(self):
        payload = {k: v for k, v in VALID_REQUEST.items() if k != "destination"}
        response = client.post("/travel/plan/stream", json=payload)
        assert response.status_code == 422

    def test_invalid_budget_type_returns_422(self):
        payload = {**VALID_REQUEST, "budget": "too-much"}
        response = client.post("/travel/plan/stream", json=payload)
        assert response.status_code == 422

    def test_empty_request_body_returns_422(self):
        response = client.post("/travel/plan/stream", json={})
        assert response.status_code == 422
