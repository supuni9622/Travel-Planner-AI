from pydantic import BaseModel


class TravelResponse(BaseModel):
    itinerary: str