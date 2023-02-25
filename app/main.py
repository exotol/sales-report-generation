import uvicorn
from fastapi import FastAPI


def app_factory() -> FastAPI:
    app = FastAPI()
    return app


def run_server():
    uvicorn.run(
        "main:app_factory",
        host="0.0.0.0",
        port=10_004,
        access_log=True,
        log_level="info",
        reload=True,
        factory=True
    )


if __name__ == "__main__":
    run_server()
    