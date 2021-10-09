import os
import logging

from functools import lru_cache
from pydantic import BaseSettings

logger = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMNET", "dev")
    testing: int = os.getenv("TESTING", 0)


@lru_cache
def get_settings() -> BaseSettings:
    logger.info("Loading applications configuration...")
    return Settings()
