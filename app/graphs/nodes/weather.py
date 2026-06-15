from app.graphs.state import TravelState


def get_weather(
    state: TravelState,
):
    destination = state["destination"]

    return {
        "weather": f"{destination}: 28°C and sunny"
    }