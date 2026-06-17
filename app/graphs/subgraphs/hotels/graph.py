from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graphs.state import TravelState

from app.tools.hotels import get_hotels


def find_hotels(
    state: TravelState,
):
    advice = state.get(
        "travel_advice",
        []
    )

    hotels = get_hotels.invoke(
        {
            "city": state["destination"]
        }
    )

    if any(
        "public transportation" in tip.lower()
        for tip in advice
    ):
        hotels = [
            f"{hotel} (Near subway)"
            for hotel in hotels
        ]

    return {
        "hotels": hotels
    }


hotel_builder = StateGraph(
    TravelState
)

hotel_builder.add_node(
    "find_hotels",
    find_hotels,
)

hotel_builder.add_edge(
    START,
    "find_hotels",
)

hotel_builder.add_edge(
    "find_hotels",
    END,
)

hotel_graph = hotel_builder.compile()


def run_hotel_agent(
    state: TravelState,
):
    result = hotel_graph.invoke(
        state
    )

    return {
        "hotels": result["hotels"]
    }