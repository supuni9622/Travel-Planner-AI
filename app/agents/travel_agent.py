from langchain.agents import create_agent

from app.models.llm import get_llm

from app.tools.weather import get_weather
from app.tools.hotels import get_hotels
from app.tools.flights import get_flights

llm = get_llm()

# agent -> model + tools + instructions
travel_agent = create_agent(
    model=llm,
    tools=[
        get_weather,
        get_hotels,
        get_flights,
    ],
    system_prompt="""
    You are an expert travel assistant.

    Use tools whenever needed.

    Provide concise answers.
    """,
)