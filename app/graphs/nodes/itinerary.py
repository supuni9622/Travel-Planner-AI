from app.graphs.state import (
    TravelState,
)

def generate_itinerary(
    state: TravelState,
):
    itinerary = f"""
    Destination: {state["destination"]}

    Weather:
        {state["weather"]}

    Flights:
        {state["flights"]}

    Hotels:
        {state["hotels"]}
    """

    return {
        "itinerary": itinerary
    }