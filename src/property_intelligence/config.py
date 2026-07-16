from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    psycopg_database_url: str

    mlflow_tracking_uri: str = "http://localhost:5000"
    model_name: str = "france-dvf-valuation"
    model_alias: str = "champion"

    data_dir: Path = Path("./data")
    model_dir: Path = Path("./models")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    settings.model_dir.mkdir(parents=True, exist_ok=True)
    return settings
