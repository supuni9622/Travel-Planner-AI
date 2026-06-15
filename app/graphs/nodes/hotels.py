from app.graphs.state import (
    TravelState,
)


# def find_hotels(
#     state: TravelState,
# ):
#     destination = state["destination"]

#     hotels = [
#         f"{destination} Hotel Avani",
#         f"{destination} Hotel ABC",
#     ]

#     return {
#         "hotels": hotels
#     }

# Simulate failure
def find_hotels(state: TravelState):
    destination = state["destination"]

    if state["retry_count"] == 0:
        hotels = []
    else:
        hotels = [
            f"{destination} Hotel Avani",
            f"{destination} Hotel ABC",
        ]

    return {
        "hotels": hotels
    }