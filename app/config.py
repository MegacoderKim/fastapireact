import os
import logging

from functools import lru_cache
from pydantic import BaseSettings, AnyUrl

logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache
def get_settings() -> BaseSettings:
    logger.info("Loading applications configuration...")
    return Settings()
