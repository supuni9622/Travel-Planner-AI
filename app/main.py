from app.services.travel_planner import (
    generate_travel_plan,
)
from app.tools.weather import get_weather
from app.tools.flights import get_flights
from app.tools.hotels import get_hotels


def main():
    result = generate_travel_plan(
        """
        I want a budget trip to Thailand for 10 days.
        I enjoy beaches and nightlife.
        My budget is $1200.
        """
    )

    print(result)
    print(type(result))

    #why invoke? LangChain tools implement a common interface: tool.invoke, llm.invoke 
    result_weather = get_weather.invoke(
        {"city": "Tokyo"}
    )

    print(result_weather)
    #This schema is what the model sees. Tools are APIs for LLMs. Human reads swagger docs, llm reads tool schemas. 
    print(get_weather.args_schema.model_json_schema())

    result_hotels= get_hotels.invoke(
         {"city": "Tokyo"}
    )

    result_flights = get_flights.invoke(
        {
        "origin": "Colombo",
        "destination": "Tokyo"
    }
    )

    print(result_hotels)
    print(result_flights)


if __name__ == "__main__":
    main()