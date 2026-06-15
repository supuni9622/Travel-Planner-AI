from typing import TypedDict

#graph schema
class TravelState(TypedDict):
    destination: str
    budget: int
    interests: list[str]

    flights: list[str]
    hotels: list[str]

    total_cost: int

    itinerary: str
