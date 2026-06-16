from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graphs.state import TravelState

from app.graphs.nodes.aggregate import aggregate_results
from app.graphs.nodes.budget import check_budget
from app.graphs.nodes.itinerary import generate_itinerary
from app.graphs.nodes.revise import revise_plan
from app.graphs.nodes.approval import request_approval
from app.graphs.nodes.approval_router import route_approval


builder = StateGraph(TravelState)

builder.add_node(
    "aggregate_results",
    aggregate_results,
)

builder.add_node(
    "generate",
    generate_itinerary,
)

builder.add_node(
    "revise",
    revise_plan,
)

builder.add_node(
    "request_approval",
    request_approval,
)

builder.add_edge(
    START,
    "aggregate_results",
)

builder.add_conditional_edges(
    "aggregate_results",
    check_budget,
    {
        "generate": "generate",
        "revise": "revise",
    },
)

builder.add_edge(
    "generate",
    "request_approval",
)

builder.add_conditional_edges(
    "request_approval",
    route_approval,
    {
        "approved": END,
        "revise": "revise",
    },
)

builder.add_edge(
    "revise",
    END,
)

itinerary_graph = builder.compile()