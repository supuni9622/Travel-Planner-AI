from pydantic import BaseModel, Field


class TravelPlan(BaseModel):
    destination: str = Field(
        description="The destination country or city."
    )

    days: int = Field(
        description="Number of days for the trip."
    )

    budget: int = Field(
        description="Total budget in USD."
    )

    interests: list[str] = Field(
        description="User interests."
    )