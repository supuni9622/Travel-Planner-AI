# For llm-powered supervisor instead of rule-based supervisor

#Architecture

# Current:
# User
#   ↓
# Rule-Based Supervisor
#   ↓
# Agents

# New:
# User
#   ↓
# LLM Supervisor
#   ↓
# Agents

# The graph stays the same.
# Only the supervisor changes.

from pydantic import BaseModel, Field


class SupervisorDecision(BaseModel):
    next_agents: list[str] = Field(
        description="Agents required to satisfy the request."
    )