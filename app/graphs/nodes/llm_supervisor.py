# for llm-powered supervisor-executer pattern

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

from app.graphs.state import TravelState

from app.models.llm import get_llm

from app.graphs.schemas.supervisor import (
    SupervisorDecision,
)

from app.prompts.supervisor import (
    SUPERVISOR_SYSTEM_PROMPT,
)


def supervisor(
    state: TravelState,
):
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        SupervisorDecision
    )

    result = structured_llm.invoke(
        [
            SystemMessage(
                content=SUPERVISOR_SYSTEM_PROMPT
            ),
            HumanMessage(
                content=state["user_query"]
            ),
        ]
    )

    return {
        "next_agents": result.next_agents
    }