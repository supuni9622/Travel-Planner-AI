from app.graphs.state import TravelState


def revise_plan(state: TravelState):
    return {
        "itinerary": (
            f"Budget exceeded.\n"
            f"Available budget: ${state['budget']}\n"
            f"Required budget: ${state['total_cost']}\n"
            f"Please increase your budget "
            f"or choose another destination."
        )
    }