from app.graphs.state import TravelState


def weather_warning(
    state: TravelState,
):
    return {
        "warnings": [
            "Heavy rain expected this week."
        ]
    }