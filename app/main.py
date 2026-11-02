from fastapi import FastAPI

from app.api.routes import documents, health
from app.config import get_settings


def create_app() -> FastAPI:
    # Load settings here so a missing env var fails at startup, not on first request.
    # settings = get_settings()

    app = FastAPI(title="legal-agent")
    # app.state.settings = settings

    app.include_router(health.router)
    app.include_router(documents.router)
    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:create_app", factory=True, host="127.0.0.1", port=8000, reload=True)
