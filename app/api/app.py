from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.travel import (
    router as travel_router,
)

app = FastAPI(
    title="Travel Planner AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
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