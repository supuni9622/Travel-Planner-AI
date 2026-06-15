from app.services.travel_planner import (
    generate_travel_plan,
)
from app.tools.weather import get_weather
from app.tools.flights import get_flights
from app.tools.hotels import get_hotels
from app.agents.travel_agent import (
    travel_agent,
)
from app.models.llm import get_llm


def main():
    #step 1 - just llm

    # result = generate_travel_plan(
    #     """
    #     I want a budget trip to Thailand for 10 days.
    #     I enjoy beaches and nightlife.
    #     My budget is $1200.
    #     """
    # )

    # print(result)
    # print(type(result))

    #Step 2 - tool calling 

    #why invoke? LangChain tools implement a common interface: tool.invoke, llm.invoke 
    # result_weather = get_weather.invoke(
    #     {"city": "Tokyo"}
    # )

    #print(result_weather)
    #This schema is what the model sees. Tools are APIs for LLMs. Human reads swagger docs, llm reads tool schemas. 
    # print(get_weather.args_schema.model_json_schema())

    # result_hotels= get_hotels.invoke(
    #      {"city": "Tokyo"}
    # )

    # result_flights = get_flights.invoke(
    #     {
    #     "origin": "Colombo",
    #     "destination": "Tokyo"
    # }
    # )

    # print(result_hotels)
    # print(result_flights)

    # Step 3 - agents
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

    #Agent Event Streaming
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

if __name__ == "__main__":
    main()