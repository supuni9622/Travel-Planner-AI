from mcp.server.fastmcp import FastMCP
from tools.hotels import get_hotels

# Using existing tools in our langgrpah project - because we should never repeat the same business logic implementation
# from app.tools.hotels import (
#     get_hotels,
# )

# from app.tools.flights import (
#     get_flights,
# )

# from app.tools.weather import (
#     get_weather,
# )


mcp = FastMCP(
    "Travel Planner"
)

@mcp.tool()
def search_hotels(
    city: str,
) -> list[str]:
    """
    Find hotels in a city.
    """

    return get_hotels(city)
    # return get_hotels.invoke(
    #     {"city": city}
    # )

@mcp.tool()
def search_flights(
    origin: str,
    destination: str,
):
    return [
        "Flight A",
        "Flight B"
    ]
    # return get_flights.invoke(
    #     {
    #         "origin": origin,
    #         "destination": destination,
    #     }
    # )

@mcp.tool()
def get_weather(
    city: str,
):
    return {
        "temperature": 24,
        "condition": "Sunny"
    }
    # return get_weather.invoke(
    #     {"city": city}
    # )

#resources
@mcp.resource(
    "travel://tokyo-guide"
)
def tokyo_guide():
    return """
    Visit Shibuya.
    Explore Akihabara.
    """

# prompts
@mcp.prompt()
def itinerary_prompt(
    destination: str,
):
    return f"""
    Create a travel itinerary for {destination}.
    """

if __name__ == "__main__":
    mcp.run()