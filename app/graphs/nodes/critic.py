from app.graphs.state import TravelState


def critique_itinerary(
    state: TravelState,
):
    issues = []

    if state["total_cost"] > state["budget"]:
        issues.append(
            "Trip exceeds budget."
        )

    if not state["weather"]:
        issues.append(
            "Weather information missing."
        )

    if not state["hotels"]:
        issues.append(
            "No hotels selected."
        )

    if not state["flights"]:
        issues.append(
            "No flights selected."
        )

    return {
        "critique": "\n".join(issues)
    }