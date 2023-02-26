import uvicorn
from typing import Any, Dict
from fastapi import FastAPI, Depends
from app.api.v1.api import config_router_v1
from app.sales_report_log.logger import get_log_config
from app.config import settings


def config_routers(app: FastAPI) -> None:
    app.include_router(config_router_v1())


def app_factory() -> FastAPI:
    app = FastAPI()
    config_routers(app)
    return app


def run_server(log_config: Dict[str, Any]):
    uvicorn.run(
        "main:app_factory",
        host=settings.UVICORN_SERVER_HOST,
        port=settings.UVICORN_SERVER_PORT,
        access_log=settings.UVICORN_SERVER_ACCESS_LOG,
        log_level=settings.UVICORN_SERVER_LOG_LEVEL,
        reload=settings.UVICORN_SERVER_RELOAD,
        factory=settings.UVICORN_SERVER_FACTORY,
        log_config=log_config,
    )


if __name__ == "__main__":
    run_server(log_config=get_log_config())
