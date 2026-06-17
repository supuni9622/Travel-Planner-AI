from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings,
)


embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./db/travel",
    embedding_function=embeddings,
)


retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 3
    }
)