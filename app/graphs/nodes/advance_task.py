# Task couter in planner-executer pattern

from app.graphs.state import TravelState


def advance_task(
    state: TravelState,
):
    return {
        "current_task_index":
        state["current_task_index"] + 1
    }