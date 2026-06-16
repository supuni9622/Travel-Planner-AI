from app.graphs.state import TravelState


def route_agents(
    state: TravelState,
):
    return state["next_agents"]