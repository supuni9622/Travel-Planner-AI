from fastapi import APIRouter

from app.api.schemas.request import (
    TravelRequest,
)

from app.api.schemas.response import (
    TravelResponse,
)

from app.services.travel_service import (
    generate_trip,stream_trip
)
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.post(
    "/plan",
    response_model=TravelResponse,
)
def plan_trip(
    request: TravelRequest,
):
    itinerary = generate_trip(
        request
    )

    return TravelResponse(
        itinerary=itinerary
    )

@router.post("/plan/stream")
def plan_trip_stream(
    request: TravelRequest,
):
    return StreamingResponse(
        stream_trip(request),
        media_type="text/event-stream",
    )