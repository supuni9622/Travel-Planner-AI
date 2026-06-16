from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graphs.state import TravelState

from app.graphs.nodes.supervisor import (
    supervisor,
)

from app.graphs.nodes.router import (
    route_agents,
)

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
    run_itinerary_agent,
)

from app.memory.checkpointer import (
    checkpointer,
)


builder = StateGraph(TravelState)

builder.add_node(
    "supervisor",
    supervisor,
)

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
    run_itinerary_agent,
)

builder.add_edge(
    START,
    "supervisor",
)

builder.add_conditional_edges(
    "supervisor",
    route_agents,
)

builder.add_edge(
    "flight_agent",
    END,
)

builder.add_edge(
    "hotel_agent",
    END,
)

builder.add_edge(
    "weather_agent",
    END,
)

builder.add_edge(
    "itinerary_agent",
    END,
)

travel_graph = builder.compile(
    checkpointer=checkpointer,
)