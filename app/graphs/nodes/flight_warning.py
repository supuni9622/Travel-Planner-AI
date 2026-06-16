from app.graphs.state import TravelState


def flight_warning(
    state: TravelState,
):
    return {
        "warnings": [
            "Flight prices are unusually high."
        ]
    }