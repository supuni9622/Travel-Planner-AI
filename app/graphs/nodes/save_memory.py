from app.graphs.state import TravelState

from app.memory.long_term import (
    save_user_profile,
)


def save_memory(
    state: TravelState,
):
    profile = state.get(
        "user_profile",
        {}
    )

    destination = state["destination"]

    profile["interests"] = state.get(
        "interests",
        []
    )

    profile["preferred_budget"] = state.get(
        "budget",
        0
    )

    profile["favorite_season"] = state.get(
        "favorite_season",
        ""
    )

    profile["preferred_hotel_type"] = state.get(
        "preferred_hotel_type",
        ""
    )

    visited = profile.get(
        "visited_destinations",
        []
    )

    if destination not in visited:
        visited.append(destination)

    profile["visited_destinations"] = visited

    budgets = profile.get(
        "budget_history",
        []
    )

    budgets.append(
        state.get(
            "budget",
            0
        )
    )

    profile["budget_history"] = budgets

    profile["average_budget"] = round(
        sum(budgets) / len(budgets),
        2
    )

    save_user_profile(
        state["user_id"],
        profile,
    )

    return {}