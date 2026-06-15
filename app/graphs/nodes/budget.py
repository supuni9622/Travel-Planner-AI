from app.graphs.state import (
    TravelState,
)

# Budget router
#This node does not update state.
# It decides the route.
def check_budget(
    state: TravelState,
) -> str:
    if state["total_cost"] <= state["budget"]:
        return "generate"

    return "revise"