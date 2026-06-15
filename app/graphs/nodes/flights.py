from app.graphs.state import (
    TravelState,
)


def find_flights(
    state: TravelState,
):
    destination = state["destination"]

    flights = [
        f"Colombo → {destination} - $650"
    ]

    return {
        "flights": flights
    }