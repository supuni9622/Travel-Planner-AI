from langgraph.types import interrupt

from app.graphs.state import TravelState


def request_approval(
    state: TravelState,
):
    #interrupt - pauses execution and returns control to the application.
    approval = interrupt(
        {
            "message": (
                "Approve this itinerary?"
            ),
            "itinerary": state["itinerary"],
        }
    )

    return {
        "approval_status": approval
    }