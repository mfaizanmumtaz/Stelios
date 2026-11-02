from functools import lru_cache
from typing import Literal

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Required: no defaults, so a missing env var fails at startup.
    # min_length=1 also rejects an empty value copied straight from .env.example.
    environment: Literal["local", "staging", "production"]
    database_url: str = Field(min_length=1)
    openai_api_key: SecretStr = Field(min_length=1)
    anthropic_api_key: SecretStr = Field(min_length=1)
    pinecone_api_key: SecretStr = Field(min_length=1)

    db_health_timeout_seconds: float = 2.0
    llm_request_timeout_seconds: float = 60.0


@lru_cache
def get_settings() -> Settings:
    return Settings()
