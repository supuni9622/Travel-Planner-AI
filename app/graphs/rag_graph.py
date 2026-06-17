from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graphs.state import TravelState

from app.graphs.nodes.llm_supervisor import supervisor
from app.graphs.nodes.router import route_agents

from app.graphs.subgraphs.flights.graph import run_flight_agent
from app.graphs.subgraphs.hotels.graph import run_hotel_agent
from app.graphs.subgraphs.weather.graph import run_weather_agent
from app.graphs.subgraphs.itinerary.graph import generate_itinerary
from app.graphs.nodes.retrieve_context import retrieve_context

from app.memory.checkpointer import checkpointer


builder = StateGraph(TravelState)

builder.add_node("supervisor", supervisor)

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
    generate_itinerary,
)

#RAG Retrieve
builder.add_node(
    "retrieve_context",
    retrieve_context,
)

builder.add_node(
    "aggregate_results",
    lambda state: {}
)

builder.add_edge(
    START,
    "supervisor",
)

#Your conditional edges should explicitly declare allowed destinations
builder.add_conditional_edges(
    "supervisor",
    route_agents,
    {
        "flight_agent": "flight_agent",
        "hotel_agent": "hotel_agent",
        "weather_agent": "weather_agent",
    },
)
builder.add_edge(
    "flight_agent",
    "aggregate_results",
)

builder.add_edge(
    "hotel_agent",
    "aggregate_results",
)

builder.add_edge(
    "weather_agent",
    "aggregate_results",
)

builder.add_edge(
    "aggregate_results",
    "retrieve_context",
)

builder.add_edge(
    "retrieve_context",
    "itinerary_agent",
)

builder.add_edge(
    "itinerary_agent",
    END,
)

travel_graph = builder.compile(
    checkpointer=checkpointer,
)