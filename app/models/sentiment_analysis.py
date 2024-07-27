from sqlalchemy import String, DateTime
from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base


class SentimentAnalysis(Base):
    """
        Represents a sentiment analysis record in the database.

        Attributes:
            id (int): The primary key of the record.
            user_input (str): The text input provided by the user for sentiment analysis.
            sentiment (str): The sentiment label resulting from the analysis.
            timestamp (datetime): The timestamp when the record was created.
                                  Defaults to the current date and time.
    """

    __tablename__ = "sentiment_analyses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_input: Mapped[str] = mapped_column(String(128))
    sentiment: Mapped[str] = mapped_column(String(128))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
