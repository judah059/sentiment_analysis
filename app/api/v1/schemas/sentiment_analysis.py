from pydantic import BaseModel, Field


class UserInput(BaseModel):
    """
    Represents the input provided by the user for sentiment analysis.

    Attributes:
        user_input (str): The text input provided by the user.
                          Must be between 1 and 128 characters.
    """
    user_input: str = Field(..., min_length=1, max_length=128)


class AnalyzedInputResponse(BaseModel):
    """
    Represents the response from the sentiment analysis.

    Attributes:
        label (str): The sentiment label (e.g., "NEGATIVE", "POSITIVE").
        score (float): The confidence score of the sentiment analysis.
    """
    label: str
    score: float
