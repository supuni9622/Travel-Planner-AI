from pydantic import BaseModel


class TravelRequest(BaseModel):
    user_id: str
    thread_id: str

    destination: str
    budget: int

    interests: list[str]

    user_query: str