from app.graphs.state import (
    TravelState,
)


def find_hotels(
    state: TravelState,
):
    destination = state["destination"]

    hotels = [
        f"{destination} Hotel Avani",
        f"{destination} Hotel ABC",
    ]

    return {
        "hotels": hotels
    }