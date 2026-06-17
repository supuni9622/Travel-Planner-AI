from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graphs.state import TravelState

from app.graphs.nodes.aggregate import aggregate_results
from app.graphs.nodes.budget import check_budget
from app.graphs.nodes.itinerary import generate_itinerary
from app.graphs.nodes.revise import revise_plan
from app.graphs.nodes.approval import request_approval
from app.graphs.nodes.approval_router import route_approval
from app.graphs.nodes.critic import critique_itinerary
from app.graphs.nodes.increment_reflection import increment_reflection
from app.graphs.nodes.reflection_router import route_reflection

from app.models.llm import get_llm

builder = StateGraph(TravelState)

builder.add_node(
    "aggregate_results",
    aggregate_results,
)

builder.add_node(
    "generate",
    generate_itinerary,
)

builder.add_node(
    "revise",
    revise_plan,
)

builder.add_node(
    "request_approval",
    request_approval,
)

builder.add_node(
    "critic",
    critique_itinerary,
)

builder.add_node(
    "increment_reflection",
    increment_reflection,
)

builder.add_edge(
    START,
    "aggregate_results",
)

builder.add_conditional_edges(
    "aggregate_results",
    check_budget,
    {
        "generate": "generate",
        "revise": "revise",
    },
)
# Since we do critic now
# builder.add_edge(
#     "generate",
#     "request_approval",
# )

builder.add_edge(
    "generate",
    "critic",
)

builder.add_conditional_edges(
    "critic",
    route_reflection,
    {
        "approved": "request_approval",
        "revise": "increment_reflection",
        "human_review": "request_approval",
    },
)

builder.add_edge(
    "increment_reflection",
    "generate",
)

builder.add_conditional_edges(
    "request_approval",
    route_approval,
    {
        "approved": END,
        "revise": "revise",
    },
)

builder.add_edge(
    "revise",
    END,
)

itinerary_graph = builder.compile()

#Deterministic formatting logic

# def run_itinerary_agent(state):
#     result = itinerary_graph.invoke(state)

#     allowed_keys = {
#         "itinerary",
#         "critique",
#         "reflection_count",
#         "approval_status",
#     }

#     return {
#         key: value
#         for key, value in result.items()
#         if key in allowed_keys
#     }


#Deterministic formatting logic

# def generate_itinerary(
#     state: TravelState,
# ):
#     advice = "\n".join(
#         f"- {item}"
#         for item in state["travel_advice"]
#     )

#     itinerary = f"""
#         Destination: {state["destination"]}

#         Advice:
#         {advice}

#         Flights:
#         {state["flights"]}

#         Hotels:
#         {state["hotels"]}

#         Weather:
#         {state["weather"]}
#         """

#     return {
#         "itinerary": itinerary
#     }

# With RAG context


def generate_itinerary(
    state: TravelState,
):
    llm = get_llm()

    context = state.get(
        "retrieved_context",
        ""
    )

    advice = "\n".join(
        f"- {item}"
        for item in state["travel_advice"]
    )

    profile = state.get(
    "user_profile",
    {}
)

    prompt = f"""
    Use the travel information below to create a personalized itinerary.

    User Preferences:
    {profile}

    Retrieved Context:
    {context}

    Destination:
    {state["destination"]}

    Interests:
    {", ".join(state["interests"])}

    Travel Advice:
    {advice}

    Flights:
    {state["flights"]}

    Hotels:
    {state["hotels"]}

    Weather:
    {state["weather"]}
    """

    response = llm.invoke(prompt)

    return {
        "itinerary": response.content
    }