# For LLM powered planning

# Architecture Evolution

# Before:
# User Query
#     ↓
# Rule-Based Planner
#     ↓
# Task List

# After:
# User Query
#     ↓
# LLM Planner
#     ↓
# Structured Task List

# The graph remains unchanged.
# Only the planner node changes.

from pydantic import BaseModel, Field


class Task(BaseModel):
    task: str = Field(
        description="Task identifier"
    )

    reason: str = Field(
        description="Why this task is needed"
    )


class TravelPlan(BaseModel):
    tasks: list[Task]