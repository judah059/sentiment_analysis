from fastapi import APIRouter, Request, Form, Depends
from fastapi.openapi.models import Response
from fastapi.templating import Jinja2Templates
from fastapi import Form
from sqlalchemy.orm import Session

from app.api.v1.schemas.sentiment_analysis import UserInput
from app.database import get_db
from app.services.sentiment_analysis import process_user_input
from app.settings.config import get_config


config = get_config()

router = APIRouter(prefix="/api/v1")

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_user_form(
        request: Request
) -> templates.TemplateResponse:
    """
        Render the sentiment analysis form.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            TemplateResponse: Renders the "sentiment_analysis.html" template with the initial form.
    """
    return templates.TemplateResponse("sentiment_analysis.html", {"request": request, "sentiment": None})


@router.post("/input_sentiment_analyze")
async def analyze_sentiment(
    request: Request,
    text: str = Form(...),
    db: Session = Depends(get_db)
) -> templates.TemplateResponse:
    """
        Analyze the sentiment of the input text and render the results.

        Args:
            request (Request): The incoming HTTP request.
            text (str): The input text to be analyzed for sentiment.
            db (Session): The database session dependency.

        Returns:
            TemplateResponse: Renders the "sentiment_analysis.html" template with the analysis results or error message.
    """

    try:
        user_input = UserInput(user_input=text)
        response = await process_user_input(db=db, user_input=user_input.user_input)
        return templates.TemplateResponse("sentiment_analysis.html", {
            "request": request,
            "text": user_input.user_input,
            "sentiment": response,
        })
    except ValueError as e:
        return templates.TemplateResponse("sentiment_analysis.html", {
            "request": request,
            "error": True,
            "error_text": e,
        })
