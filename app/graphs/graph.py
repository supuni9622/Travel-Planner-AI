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
from app.graphs.nodes.budget import (
    check_budget,
)

from app.graphs.nodes.revise import (
    revise_plan,
)
from app.graphs.nodes.weather import (
    get_weather,
)
from app.graphs.nodes.aggregate import aggregate_results
from app.graphs.nodes.retry import increment_retry
from app.graphs.nodes.failure import hotel_failure
from app.graphs.nodes.validation import validate_hotels

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
builder.add_node(
    "revise",
    revise_plan,
)

builder.add_node(
    "generate",
    generate_itinerary,
)
builder.add_node(
    "get_weather",
    get_weather,
)
builder.add_node("aggregate_results", aggregate_results)

# Validation and retry nodes
builder.add_node(
    "increment_retry",
    increment_retry,
)

builder.add_node(
    "hotel_failure",
    hotel_failure,
)

#Add edges

# builder.add_edge(
#     START,
#     "find_hotels",
# )

# builder.add_edge(
#     "find_hotels",
#     "find_flights",
# )

#Create Fan-Out
builder.add_edge(
    START,
    "find_hotels",
)

builder.add_edge(
    START,
    "find_flights",
)

builder.add_edge(
    START,
    "get_weather",
)

# builder.add_edge(
#     "find_flights",
#     "generate_itinerary",
# )

# builder.add_edge(
#     "generate_itinerary",
#     END,
# )

# Fan-in
# builder.add_edge("find_hotels", "aggregate_results")

# Add validation and retry for hotel finding failure
builder.add_conditional_edges(
    "find_hotels",
    validate_hotels,
    {
        "continue": "aggregate_results",
        "retry": "increment_retry",
        "failed": "hotel_failure",
    },
)
builder.add_edge(
    "increment_retry",
    "find_hotels",
)
builder.add_edge(
    "hotel_failure",
    END,
)

builder.add_edge("find_flights", "aggregate_results")
builder.add_edge("get_weather", "aggregate_results")

# Adding conditional edges instead of lineor workflow
# builder.add_conditional_edges(
#     "find_flights",
#     check_budget,
#     {
#         "generate": "generate",
#         "revise": "revise",
#     },
# )

# Conditional routing in parallel workflow
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
    END,
)

builder.add_edge(
    "revise",
    END,
)

#Compile
travel_graph = builder.compile()

