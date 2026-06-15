from app.tools.weather import get_weather
from app.tools.flights import get_flights
from app.tools.hotels import get_hotels


def test_tools():
    #Step 2 - tool calling 

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
