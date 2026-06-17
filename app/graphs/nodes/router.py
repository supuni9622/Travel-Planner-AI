from app.graphs.state import TravelState

VALID_AGENTS = {
    "flight_agent",
    "hotel_agent",
    "weather_agent",
}


def route_agents(state: TravelState):
    agents = [
        agent
        for agent in state.get("next_agents", [])
        if agent in VALID_AGENTS
    ]

    return {
        "next_agents": agents
    }