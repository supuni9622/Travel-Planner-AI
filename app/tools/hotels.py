from langchain_core.tools import tool


@tool
def get_hotels(city: str) -> list[str]:
    #Why Docstring Matters - The tool description is shown to the LLM.
    #becomes part of the tool schema. Poor descriptions lead to poor tool usage.
    """
    Get the holels information for a city.
    """

    mock_hotels = {
        "tokyo": ["Hotel Avani", "Hotel ABC"],
        "paris": ["Hotel Paris", "Hotel Hotel France"],
        "bangkok": ["Hotel Thailand", "Hotel Anantara"]
    }

    return mock_hotels.get(
        city.lower(),
        "Hotels data unavailable."
    )