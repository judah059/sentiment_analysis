from transformers import pipeline

from app.api.v1.schemas.sentiment_analysis import AnalyzedInputResponse


async def get_analyzed_input_response(
        user_input: str
) -> list[AnalyzedInputResponse]:
    """
        Analyze the sentiment of the given user input using a pre-trained sentiment analysis model.

        Args:
            user_input (str): The input text to be analyzed for sentiment.

        Returns:
            list[AnalyzedInputResponse]: A list of AnalyzedInputResponse objects containing
                                         the sentiment analysis results, which includes the
                                         sentiment label and the confidence score.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(user_input)
