from sqlalchemy.orm import Session

from app.ai_services.sentiment_analysis import get_analyzed_input_response
from app.models.sentiment_analysis import SentimentAnalysis


async def save_user_input_and_sentiment_analysis(
        sentiment: str,
        user_input: str,
        db: Session
) -> None:
    """
        Save the user input and its sentiment analysis result to the database.

        Args:
            sentiment (str): The sentiment label of the user input.
            user_input (str): The text input provided by the user.
            db (Session): The database session for database operations.

        Returns:
            None
    """

    sentiment_analysis_object = SentimentAnalysis(
        user_input=user_input,
        sentiment=sentiment,
    )

    db.add(sentiment_analysis_object)
    db.commit()


async def process_user_input(
        db: Session,
        user_input: str,
) -> str:
    """
        Process the user input for sentiment analysis and save the result to the database.

        Args:
            db (Session): The database session for database operations.
            user_input (str): The text input provided by the user.

        Returns:
            str: The sentiment label of the analyzed user input.
    """

    analyzed_input_response = await get_analyzed_input_response(user_input=user_input)
    sentiment = analyzed_input_response[0]['label']
    await save_user_input_and_sentiment_analysis(
        user_input=user_input,
        sentiment=sentiment,
        db=db,
    )
    return sentiment
