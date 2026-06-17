# For planner-executer pattern

from app.graphs.state import TravelState


def planner(
    state: TravelState,
):
    query = state["user_query"].lower()

    tasks = []

    #Later, we'll replace rules with an LLM.

    if "flight" in query or "trip" in query:
        tasks.append(
            {
                "id": 1,
                "task": "find_flights",
                "status": "pending",
            }
        )

    if "hotel" in query or "trip" in query:
        tasks.append(
            {
                "id": 2,
                "task": "find_hotels",
                "status": "pending",
            }
        )

    if "weather" in query or "trip" in query:
        tasks.append(
            {
                "id": 3,
                "task": "get_weather",
                "status": "pending",
            }
        )

    tasks.append(
        {
            "id": 4,
            "task": "generate_itinerary",
            "status": "pending",
        }
    )

    return {
        "tasks": tasks,
        "current_task_index": 0,
    }