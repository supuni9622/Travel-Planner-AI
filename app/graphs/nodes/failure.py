from app.graphs.state import TravelState

# Failure node
def hotel_failure(
    state: TravelState,
):
    return {
        "itinerary": (
            "Unable to find hotels "
            "after multiple attempts."
        )
    }