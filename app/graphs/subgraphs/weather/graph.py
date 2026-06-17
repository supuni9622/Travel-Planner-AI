from langgraph.graph import (
    START,
    END,
    StateGraph,
)
from app.graphs.state import (
    TravelState,
)
from app.graphs.nodes.weather import (
    get_weather,
)

weather_builder = StateGraph(TravelState)

weather_builder.add_node(
    "get_weather",
    get_weather,
)

weather_builder.add_edge(
    START,
    "get_weather",
)

weather_builder.add_edge(
    "get_weather",
    END,
)

weather_graph = weather_builder.compile()

#Nodes return only the changes but graphs return the whole state
# In parallel execusion this lead to conflicts 
# Quick fix -> convert the subgrpah into node
# Long term fix -> manage seperate states for subgraphs and merge later

def run_weather_agent(state):
    result = weather_graph.invoke(state)

    advice = []

    weather = result["weather"].lower()

    if "rain" in weather:
        advice.append(
            "Choose hotels near public transportation."
        )

    return {
        "weather": result["weather"],
        "travel_advice": advice,
    }