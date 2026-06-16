from app.graphs.state import TravelState


def increment_reflection(
    state: TravelState,
):
    return {
        "reflection_count":
        state["reflection_count"] + 1
    }