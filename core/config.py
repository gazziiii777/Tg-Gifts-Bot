from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()


class Settings(BaseSettings):
    DB_URL: str = os.getenv("DB_URL")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_NAME: str = os.getenv("DB_NAME")
    TELEGRAM_API_ID: str = os.getenv("TELEGRAM_API_ID")
    TELEGRAM_API_HASH: str = os.getenv("TELEGRAM_API_HASH")
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgres://{self.DB_USER}:{self.DB_PASS}@{self.DB_URL}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()
