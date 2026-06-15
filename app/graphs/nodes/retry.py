from app.graphs.state import TravelState


def increment_retry(
    state: TravelState,
):
    return {
        "retry_count": state["retry_count"] + 1
    }