from app.graphs.state import (
    TravelState,
)

def generate_itinerary(
    state: TravelState,
):
    
    warnings = "\n".join(
        f"- {warning}"
        for warning in state["warnings"]
    )

    itinerary = f"""
    Destination: {state["destination"]}

    Weather:
        {state["weather"]}

    Flights:
        {state["flights"]}
    
    Warnings:
        {warnings}


    Hotels:
        {state["hotels"]}
    """

    return {
        "itinerary": itinerary
    }
