from app.graphs.state import TravelState

from app.memory.long_term import (
    load_user_profile,
)


def load_memory(
    state: TravelState,
):

    profile = load_user_profile(
        state["user_id"]
    )

    return {
        "user_profile": profile
    }