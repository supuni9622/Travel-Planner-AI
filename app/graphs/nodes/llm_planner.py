# LLM powered planning
# Adavanced and real work usage of planner-executer pattern due to rule-based plan is limited

from app.graphs.state import TravelState
from app.graphs.schemas.planner import (
    TravelPlan,
)

from app.models.llm import get_llm

from app.prompts.planner import (
    PLANNER_SYSTEM_PROMPT,
)

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)


def planner(
    state: TravelState,
):
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        TravelPlan
    )

    result = structured_llm.invoke(
        [
            SystemMessage(
                content=PLANNER_SYSTEM_PROMPT
            ),
            HumanMessage(
                content=state["user_query"]
            ),
        ]
    )

    tasks = [
        {
            "id": index,
            "task": task.task,
            "reason": task.reason,
            "status": "pending",
        }
        for index, task in enumerate(
            result.tasks,
            start=1,
        )
    ]

    return {
        "tasks": tasks,
        "current_task_index": 0,
    }
