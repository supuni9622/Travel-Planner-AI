from langgraph.checkpoint.memory import (
    InMemorySaver,
)
from langgraph.checkpoint.postgres import (
    PostgresSaver,
)

#This stores conversation history in memory.
#this is tempory and restart when server restart
memory = InMemorySaver()

# Persistnat memory
DB_URI = (
    "postgresql://travel_user:"
    "travel_password@localhost:5432/travel_ai"
)

_checkpointer_cm = PostgresSaver.from_conn_string(DB_URI)

checkpointer = _checkpointer_cm.__enter__()