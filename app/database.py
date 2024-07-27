from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URL = "sqlite:///./sentiment_analysis.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """
        Base class for all database models.

        This class is used as a base for all models that define tables
        in the database. It extends SQLAlchemy's DeclarativeBase.
    """
    pass


def get_db():
    """
        Create a new database session and yield it.

        This function sets up the database schema if it does not already exist,
        creates a new database session, and ensures the session is closed after use.

        Yields:
            db (Session): A new database session.
    """

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
