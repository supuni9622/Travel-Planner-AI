from app.models.llm import get_llm
from app.tests.test_model import test_structured_output
from app.tests.test_tools import test_tools
from app.tests.test_agents import test_agent
from app.tests.test_streaming import test_streaming
from app.tests.test_memory import test_memory
from app.graphs.graph import (
    travel_graph,
)



def main():
   
    #step 1 - just llm
    # test_structured_output()

    # step 2 - tool calling
    # test_tools()
    
    # Step 3 - agents
    # test_agent()
    

    #4. Agent Event Streaming
    # test_streaming()

    #5. Multi-Turn Conversation with memory
    # test_memory()

    #6. Langgraph - Run the Graph

    initial_state = {
    "destination": "Tokyo",
    "budget": 500,
    "interests": ["anime", "food"],

    "hotels": [],
    "flights": [],
    "weather": "",

    "total_cost": 0,

    "itinerary": "",
    }
    result = travel_graph.invoke(initial_state)

    # see the events of graph
    for event in travel_graph.stream(initial_state):
        for node_name, updates in event.items():
            print(f"\nNode: {node_name}")
            print(f"Updates: {updates}")
            print("-" * 50)

    print(result["itinerary"])



if __name__ == "__main__":
    main()