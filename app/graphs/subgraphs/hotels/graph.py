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

hotel_builder = StateGraph(TravelState)

hotel_builder.add_node(
    "find_hotels",
    find_hotels,
)

hotel_builder.add_edge(
    START,
    "find_hotels",
)

hotel_builder.add_edge(
    "find_hotels",
    END,
)

hotel_graph = hotel_builder.compile()

#Nodes return only the changes but graphs return the whole state
# In parallel execusion this lead to conflicts 
# Quick fix -> convert the subgrpah into node
# Long term fix -> manage seperate states for subgraphs and merge later

def run_hotel_agent(state):
    result = hotel_graph.invoke(state)

    return {
        "hotels": result["hotels"],
    }