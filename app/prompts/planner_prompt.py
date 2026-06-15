from langchain_core.prompts import ChatPromptTemplate


planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert travel planner.

            Extract travel requirements from the user request.

            Return accurate information.
            """,
        ),
        (
            "human",
            """
            {user_request}
            """,
        ),
    ]
)