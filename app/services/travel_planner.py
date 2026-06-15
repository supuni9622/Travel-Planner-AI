from app.models.llm import get_llm
from app.prompts.planner_prompt import planner_prompt
from app.schemas.travel_plan import TravelPlan


def generate_travel_plan(user_request: str) -> TravelPlan:
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        TravelPlan
    )

    chain = planner_prompt | structured_llm

    response = chain.invoke(
        {
            "user_request": user_request
        }
    )

    return response