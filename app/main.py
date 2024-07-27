from fastapi import FastAPI
from app.api.v1.handlers.sentiment_analysis import router as sentiment_analysis_router


def create_app() -> FastAPI:
    """
    Creates and configures the FastAPI application for LeanGeeksAI.

    This function sets up the FastAPI application with a title, documentation URL,
    and includes the router for the LeanGeeksAI bot.

    Returns:
        FastAPI: The configured FastAPI application.
    """
    app = FastAPI(
        title="LeanGeeksAI",
        docs_url="/api/docs",
        description="",
    )

    app.include_router(sentiment_analysis_router)

    return app
