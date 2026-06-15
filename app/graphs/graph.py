from langgraph.graph import (
    START,
    END,
    StateGraph,
)
from app.graphs.state import (
    TravelState,
)
from app.graphs.nodes.hotels import (
    find_hotels,
)
from app.graphs.nodes.flights import (
    find_flights,
)
from app.graphs.nodes.itinerary import (
    generate_itinerary,
)

# create the builder
builder = StateGraph(TravelState)

#Add nodes
builder.add_node(
    "find_hotels",
    find_hotels,
)

builder.add_node(
    "find_flights",
    find_flights,
)

builder.add_node(
    "generate_itinerary",
    generate_itinerary,
)

#Add edges
builder.add_edge(
    START,
    "find_hotels",
)

builder.add_edge(
    "find_hotels",
    "find_flights",
)

builder.add_edge(
    "find_flights",
    "generate_itinerary",
)

builder.add_edge(
    "generate_itinerary",
    END,
)

#Compile
travel_graph = builder.compile()

