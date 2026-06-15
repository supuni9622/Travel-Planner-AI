from langgraph.checkpoint.memory import (
    InMemorySaver,
)

#This stores conversation history in memory.
#this is tempory and restart when server restart
memory = InMemorySaver()