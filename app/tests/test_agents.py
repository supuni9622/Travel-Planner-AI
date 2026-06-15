from app.agents.travel_agent import (
    travel_agent,
)
from app.models.llm import get_llm

def test_agent():
    response = travel_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Find hotels in Tokyo."
                    ),
                }
            ]
        }
    )

    print(response)
    #Response returns the whole conversation history and if we need to print the last message 
    print(response["messages"][-1].content)

    #debugging
    for message in response["messages"]:
        print(type(message).__name__)
        print(message)
        print("-" * 50)

    # Token streaming 
    llm = get_llm()
    for chunk in llm.stream(
        "Tell me about Tokyo."
    ):
        print(chunk.content, end="", flush=True)