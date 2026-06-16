from app.models.llm import get_llm
from app.tests.test_model import test_structured_output
from app.tests.test_tools import test_tools
from app.tests.test_agents import test_agent
from app.tests.test_streaming import test_streaming
from app.tests.test_memory import test_memory
# from app.graphs.graph_single import (
#     travel_graph,
# )
from app.graphs.graph import (travel_graph)
from langgraph.types import Command

initial_state = {
    "destination": "Tokyo",
    "budget": 2000,
    "interests": ["anime", "food"],

    "hotels": [],
    "flights": [],
    "weather": "",

    "total_cost": 0,
    "retry_count": 0,

    "itinerary": "",
    "warnings": []
    }
config = {
        "configurable": {
        "thread_id": "travel_123"
        }
    }

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
    result = travel_graph.invoke(initial_state, 
                                 config=config)

    # Observe execusion of sevents of graph
    # Important - we should use either invoke or stream - not both together

    # for event in travel_graph.stream(initial_state, config=config):
    #     for node_name, updates in event.items():
    #         print(f"\nNode: {node_name}")
    #         print(f"Updates: {updates}")
    #         print("-" * 50)

    # Resume execution after interuption
    if "__interrupt__" in result:
        print("Graph paused.")

        user_input = "approve"

        result = travel_graph.invoke(
            Command(resume=user_input),
            config=config,
        )

    # print(result["itinerary"])

    # Inspect Saved State
    snapshot = travel_graph.get_state(config)
    print(snapshot.values)
    # history = travel_graph.get_state_history(config)
    # for snapshot in history:
    #     print(snapshot.values)

    print(result["warnings"])


if __name__ == "__main__":
    main()