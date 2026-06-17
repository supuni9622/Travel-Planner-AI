#Executer router in planner-executer pattern

from app.graphs.state import TravelState


def route_task(
    state: TravelState,
):
    index = state["current_task_index"]

    if index >= len(state["tasks"]):
        return "done"

    return state["tasks"][index]["task"]

