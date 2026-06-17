# Planner-executer pattern

from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graphs.state import TravelState

from app.graphs.nodes.llm_planner import planner
from app.graphs.nodes.task_router import route_task
from app.graphs.nodes.advance_task import advance_task

from app.graphs.subgraphs.flights.graph import run_flight_agent
from app.graphs.subgraphs.hotels.graph import run_hotel_agent
from app.graphs.subgraphs.weather.graph import run_weather_agent
from app.graphs.subgraphs.itinerary.graph import run_itinerary_agent

from app.memory.checkpointer import checkpointer


builder = StateGraph(TravelState)

builder.add_node(
    "planner",
    planner,
)

builder.add_node(
    "find_flights",
    run_flight_agent,
)

builder.add_node(
    "find_hotels",
    run_hotel_agent,
)

builder.add_node(
    "get_weather",
    run_weather_agent,
)

builder.add_node(
    "generate_itinerary",
    run_itinerary_agent,
)

builder.add_node(
    "advance_task",
    advance_task,
)

builder.add_edge(
    START,
    "planner",
)

builder.add_conditional_edges(
    "planner",
    route_task,
)

builder.add_edge(
    "find_flights",
    "advance_task",
)

builder.add_edge(
    "find_hotels",
    "advance_task",
)

builder.add_edge(
    "get_weather",
    "advance_task",
)

builder.add_edge(
    "generate_itinerary",
    "advance_task",
)

builder.add_conditional_edges(
    "advance_task",
    route_task,
    {
        "find_flights": "find_flights",
        "find_hotels": "find_hotels",
        "get_weather": "get_weather",
        "generate_itinerary": "generate_itinerary",
        "done": END,
    },
)

travel_graph = builder.compile(checkpointer=checkpointer)