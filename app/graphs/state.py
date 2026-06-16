from typing import TypedDict
from operator import add
from typing import Annotated

#graph schema
class TravelState(TypedDict):
    user_query: str
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

    warnings: Annotated[ #reducers - supports multiple writers.
        list[str],
        add,
    ]
    next_agents: list[str] #Supervisor -executer pattern 
