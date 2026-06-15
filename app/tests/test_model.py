from app.services.travel_planner import (
    generate_travel_plan,
)

def test_structured_output():
     #step 1 - just llm

    result = generate_travel_plan(
        """
        I want a budget trip to Thailand for 10 days.
        I enjoy beaches and nightlife.
        My budget is $1200.
        """
    )

    print(result)
    print(type(result))
