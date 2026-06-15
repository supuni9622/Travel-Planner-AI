from langchain_core.tools import tool


@tool
def get_flights(origin: str, destination: str) -> str:
    #Why Docstring Matters - The tool description is shown to the LLM.
    #becomes part of the tool schema. Poor descriptions lead to poor tool usage.
    """
    Get the flight information from one city to another city.
    """

    mock_flights = {
        "colombo-tokyo": [{"flight":"flight1", "date":"2026.06.30", "time":"10.00pm"},
                          {"flight":"flight2", "date":"2026.07.30", "time":"05.00pm"}
                          ],
        "colombo-paris": [{"flight":"flight3", "date":"2026.06.30", "time":"10.00pm"},
                          {"flight":"flight4", "date":"2026.07.30", "time":"05.00pm"}
                          ],
        "bangkok": [{"flight":"flight5", "date":"2026.06.30", "time":"10.00pm"},
                          {"flight":"flight6", "date":"2026.07.30", "time":"05.00pm"}
                          ],
    }

    key = f"{origin.lower()}-{destination.lower()}"

    return mock_flights.get(
        key,
        "Flight data unavailable."
    )