from app.agents.travel_agent import (
    travel_agent,
)

#Add a Thread ID - Memory needs a conversation identifier.
config = {
    "configurable": {
        "thread_id": "user_123"
    }
}

def test_memory():
    response1 = travel_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "I like anime."
                }
            ]
        },
            config=config,
        )

    print(response1["messages"][-1].content)

    response2 = travel_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Plan my Tokyo trip from colombo. tell me the places to visit based on my interest"
                }
            ]
        },
        config=config,
        )

    print(response2["messages"][-1].content)
