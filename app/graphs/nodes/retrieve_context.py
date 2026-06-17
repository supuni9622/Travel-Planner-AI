from app.graphs.state import TravelState

from app.rag.retriever import (
    retriever,
)


def retrieve_context(
    state: TravelState,
):
    docs = retriever.invoke(
        state["user_query"]
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return {
        "retrieved_context": context
    }