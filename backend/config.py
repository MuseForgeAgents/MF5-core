import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    REPLICATE_API_TOKEN: str
    HUGGINGFACE_API_TOKEN: str
    DATABASE_URL: str = "sqlite:///./mf5.db"
    REDIS_URL: str = "redis://localhost:6379"
    LOG_LEVEL: str = "INFO"
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 3600

    class Config:
        env_file = ".env"

settings = Settings()
