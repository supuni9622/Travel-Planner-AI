from langgraph.graph import (
    START,
    END,
    StateGraph,
)
from app.graphs.state import (
    TravelState,
)
from app.graphs.nodes.flights import (
    find_flights,
)

flight_builder = StateGraph(TravelState)

flight_builder.add_node(
    "find_flights",
    find_flights,
)

flight_builder.add_edge(
    START,
    "find_flights",
)

flight_builder.add_edge(
    "find_flights",
    END,
)

flight_graph = flight_builder.compile()

#Nodes return only the changes but graphs return the whole state
# In parallel execusion this lead to conflicts 
# Quick fix -> convert the subgrpah into node
# Long term fix -> manage seperate states for subgraphs and merge later

def run_flight_agent(state):
    result = flight_graph.invoke(state)

    advice = []

    if result["flights"]:
        advice.append(
            "Arrive before noon on the first day."
        )

    return {
        "flights": result["flights"],
        "total_cost": result["total_cost"],
        "travel_advice": advice,
    }