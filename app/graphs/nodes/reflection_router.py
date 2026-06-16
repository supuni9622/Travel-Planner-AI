from app.graphs.state import TravelState


def route_reflection(
    state: TravelState,
):
    critique = state["critique"]

    if not critique:
        return "approved"

    if (
        state["reflection_count"]
        >= state["max_reflections"]
    ):
        return "human_review"

    return "revise"