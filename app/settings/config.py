from pydantic.v1 import BaseSettings


class Config(BaseSettings):
    """
    Configuration settings for the application.

    This class uses Pydantic's BaseSettings to define and validate
    environment variables for various services and settings.
    """

    class Config:
        """
        Pydantic configuration class.

        This class specifies the location of the environment file.
        """

        env_file = ".env"


def get_config() -> Config:
    """
    Retrieve the application configuration.

    Returns:
        Config: The application configuration settings.
    """
    return Config()
