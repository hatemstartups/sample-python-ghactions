"""Main application entry point."""

import uvicorn
from fastapi import FastAPI

from app import routers

service = FastAPI(
    title="fast api example",
    description="Example Python API V1.",
    version="v1",
)

service.include_router(routers.main.router)

if __name__ == "__main__":
    # Debug-only configuration
    uvicorn.run(service)
