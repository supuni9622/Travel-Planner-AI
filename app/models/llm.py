import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():
    provider = os.getenv("MODEL_PROVIDER", "groq")
    model_name = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    temperature = float(
        os.getenv("TEMPERATURE", "0.2")
    )

    max_tokens = int(
        os.getenv("MAX_TOKENS", "1024")
    )

    if provider == "groq":
        return ChatGroq(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    raise ValueError(
        f"Unsupported provider: {provider}"
    )