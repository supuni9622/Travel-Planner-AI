from app.graphs.state import TravelState


def route_approval(
    state: TravelState,
) -> str:
    if state["approval_status"] == "approve":
        return "approved"

    return "revise"