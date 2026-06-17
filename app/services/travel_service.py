from fastapi import HTTPException

# we can import the necessary graph to invoke here
from app.graphs.rag_graph import travel_graph

#getting fastapi request and create initial state

from app.api.schemas.request import TravelRequest
import json
from app.graphs.rag_graph import travel_graph
from app.api.schemas.request import TravelRequest



def create_state(
    request: TravelRequest,
) -> dict:
    return {
        "user_id": request.user_id,

        "destination": request.destination,
        "budget": request.budget,
        "interests": request.interests,

        "user_query": request.user_query,

        "flights": [],
        "hotels": [],
        "weather": "",

        "travel_advice": [],
        "warnings": [],

        "itinerary": "",
        "retrieved_context": "",

        "next_agents": [],

        "reflection_count": 0,
        "max_reflections": 2,

        "tasks": [],
        "current_task_index": 0,

        "retry_count": 0,
        "total_cost": 0,

        "approval_status": "approve",
        "critique": "",

        "user_profile": {},
        "memories": [],
    }


def generate_trip(
    request: TravelRequest,
) -> str:

    state = create_state(request)

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    try:
        result = travel_graph.invoke(
            state,
            config=config,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    return result["itinerary"]

#streaming 
def stream_trip(
    request: TravelRequest,
):
    state = create_state(request)

    config = {
        "configurable": {
            "thread_id": request.thread_id
        }
    }

    for event in travel_graph.stream(
        state,
        config=config,
        stream_mode="updates",
    ):
        yield (
            f"data: {json.dumps(event, default=str)}\n\n"
        )