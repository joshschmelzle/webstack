import logging

from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.staticfiles import StaticFiles

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.settings import endpoints
from app.views import home

log = logging.getLogger("uvicorn")

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)
for route in app.routes:
    if isinstance(route, APIRoute):
        endpoints.append({"path": route.path})

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(home.router)
