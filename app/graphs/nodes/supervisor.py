from app.graphs.state import TravelState

# Important: 
# We use code first.
# Later we'll replace this with an LLM.

def supervisor(
    state: TravelState,
):
    query = state["user_query"].lower()

    next_agents = []

    if any(
        word in query
        for word in ["flight", "trip", "travel"]
    ):
        next_agents.append("flight_agent")

    if any(
        word in query
        for word in ["hotel", "stay", "trip"]
    ):
        next_agents.append("hotel_agent")

    if any(
        word in query
        for word in ["weather", "trip"]
    ):
        next_agents.append("weather_agent")

    if "trip" in query:
        next_agents.append("itinerary_agent")

    return {
        "next_agents": next_agents
    }