from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graphs.state import TravelState

from app.graphs.subgraphs.flights.graph import (
    run_flight_agent,
)

from app.graphs.subgraphs.hotels.graph import (
    run_hotel_agent,
)

from app.graphs.subgraphs.weather.graph import (
    run_weather_agent,
)

from app.graphs.subgraphs.itinerary.graph import (
    itinerary_graph,
)

from app.memory.checkpointer import (
    checkpointer,
)
from langgraph.checkpoint.memory import InMemorySaver

from app.graphs.nodes.flight_warning import (
    flight_warning,
)

from app.graphs.nodes.weather_warning import (
    weather_warning,
)


builder = StateGraph(TravelState)
memory = InMemorySaver()

# Register subgraphs as nodes
builder.add_node(
    "flight_agent",
    run_flight_agent,
)

builder.add_node(
    "hotel_agent",
    run_hotel_agent,
)

builder.add_node(
    "weather_agent",
    run_weather_agent,
)

builder.add_node(
    "itinerary_agent",
    itinerary_graph,
)

builder.add_node(
    "flight_warning",
    flight_warning,
)

builder.add_node(
    "weather_warning",
    weather_warning,
)

# Fan-out
builder.add_edge(
    START,
    "flight_agent",
)

builder.add_edge(
    START,
    "hotel_agent",
)

builder.add_edge(
    START,
    "weather_agent",
)

builder.add_edge(
    START,
    "flight_warning",
)

builder.add_edge(
    START,
    "weather_warning",
)

# Fan-in
builder.add_edge(
    "flight_agent",
    "itinerary_agent",
)

builder.add_edge(
    "hotel_agent",
    "itinerary_agent",
)

builder.add_edge(
    "weather_agent",
    "itinerary_agent",
)
builder.add_edge(
    "flight_warning",
    "itinerary_agent",
)

builder.add_edge(
    "weather_warning",
    "itinerary_agent",
)

builder.add_edge(
    "itinerary_agent",
    END,
)

travel_graph = builder.compile(
    checkpointer=memory,
)