from app.agents.travel_agent import (
    travel_agent,
)

def test_streaming():
     #stream_mode="values" - to inspect state
    # stream_mode="updates" - to inspect events.
    events = travel_agent.stream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Find hotels in Tokyo.",
                }
            ]
        },
        stream_mode="updates",
    )

    for event in events:
        for node_name, node_data in event.items():
            print(f"\nNode: {node_name}")

            for message in node_data["messages"]:
                print(type(message).__name__)
                print(message.content)

        print("=" * 50)
