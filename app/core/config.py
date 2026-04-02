from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Text Analyzer API"
    CORS_ORIGINS: List[str] = ["*"]
    MODEL_CACHE_DIR: str = "./.cache/huggingface"

    class Config:
        env_file = ".env"

settings = Settings()
