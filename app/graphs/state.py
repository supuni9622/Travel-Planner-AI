from typing import TypedDict

#graph schema
class TravelState(TypedDict):
    destination: str
    budget: int
    interests: list[str]

    flights: list[str]
    hotels: list[str]

    weather: str

    total_cost: int

    retry_count: int # to prevent infinite loop

    itinerary: str
    approval_status: str
