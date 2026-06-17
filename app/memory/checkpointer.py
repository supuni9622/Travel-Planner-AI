from langgraph.checkpoint.memory import (
    InMemorySaver,
)
from langgraph.checkpoint.postgres import (
    PostgresSaver,
)
import os

#This stores conversation history in memory.
#this is tempory and restart when server restart
memory = InMemorySaver()

# Persistnat memory
# DB_URI = (
#     "postgresql://travel_user:"
#     "travel_password@localhost:5432/travel_ai"
# )


DATABASE_URL = os.getenv("DATABASE_URL")

_checkpointer_cm = PostgresSaver.from_conn_string(DATABASE_URL)

checkpointer = _checkpointer_cm.__enter__()