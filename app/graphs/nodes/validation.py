from app.graphs.state import TravelState

# Validation router
def validate_hotels(
    state: TravelState,
) -> str:
    if state["hotels"]:
        return "continue"

    if state["retry_count"] >= 2:
        return "failed"

    return "retry"

#logic
# Hotels found?
#       │
#    Yes ──► continue

# No hotels?
#       │
# Retry limit reached?
#       │
#    Yes ──► failed

#    No ──► retry