from fastapi import FastAPI

from app.api.routes.travel import (
    router as travel_router,
)

app = FastAPI(
    title="Travel Planner AI",
    version="1.0.0",
)

#Health check
# Used by:
# Kubernetes
# Docker
# Load balancers
@app.get("/health")
def health():
    return {
        "status": "ok"
    }

app.include_router(
    travel_router,
    prefix="/travel",
    tags=["travel"],
)