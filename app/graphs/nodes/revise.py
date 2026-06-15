from app.graphs.state import (
    TravelState,
)


def revise_plan(
    state: TravelState,
):
    return {
        "itinerary": (
            "Budget exceeded. "
            "Please increase budget "
            "or choose another destination."
        )
    }