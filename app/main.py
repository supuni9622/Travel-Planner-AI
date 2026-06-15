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
    result = travel_graph.invoke(
        {
            "destination": "Tokyo",
            "budget": 2000,
            "interests": ["anime"],
            "hotels": [],
            "flights": [],
            "itinerary": "",
        }
    )

    print(result["itinerary"])



if __name__ == "__main__":
    main()