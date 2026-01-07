"""
Application configuration module.

Loads database configuration from environment variables using
Pydantic BaseSettings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Attributes:
        DATABASE_HOST: Database server hostname.
        DATABASE_PORT: Database server port (default: 5432).
        DATABASE_NAME: Database name.
        DATABASE_USER: Database username.
        DATABASE_PASSWORD: Database password.
    """

    DATABASE_HOST: str
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    # Configuration for loading environment variables from .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Singleton settings instance used across the application
settings: Settings = Settings()
