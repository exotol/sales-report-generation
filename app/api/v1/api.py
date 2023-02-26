from fastapi import APIRouter
from app.api.v1.endpoints import root


def config_router_v1() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(root.router)
    return api_router
