from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    #Why Docstring Matters - The tool description is shown to the LLM.
    #becomes part of the tool schema. Poor descriptions lead to poor tool usage.
    """
    Get current weather information for a city.
    """

    mock_weather = {
        "tokyo": "28°C and sunny",
        "paris": "22°C and cloudy",
        "bangkok": "31°C and humid",
    }

    return mock_weather.get(
        city.lower(),
        "Weather data unavailable."
    )