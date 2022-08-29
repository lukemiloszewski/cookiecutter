from pydantic import BaseSettings


class Config(BaseSettings):
    """Application configuration."""

    GREETING = "HELLO, WORLD!"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


CONFIG = Config()
