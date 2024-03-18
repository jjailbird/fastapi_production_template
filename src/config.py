from typing import Any

from pydantic import PostgresDsn, RedisDsn, model_validator, validator
from pydantic_settings import BaseSettings

from src.constants import Environment


class Config(BaseSettings):
    POSTGRES_HOST: str = "db-host"
    POSTGRES_DB: str = "db"
    POSTGRES_USER: str = "db-usr"
    POSTGRES_PASSWORD: str = "db-pwd"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: PostgresDsn | None = None
    REDIS_URL: RedisDsn

    SITE_DOMAIN: str = "myapp.com"

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"

    @validator('DATABASE_URL', pre=True, always=True)
    def assemble_database_url(cls, v, values):
        if v is None:  # DATABASE_URL이 명시적으로 제공되지 않은 경우 조합하여 생성
            user = values.get('POSTGRES_USER')
            password = values.get('POSTGRES_PASSWORD')
            host = values.get('POSTGRES_HOST')
            port = values.get('POSTGRES_PORT')
            db = values.get('POSTGRES_DB')
            return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"
        return v

    @model_validator(mode="after")
    def validate_sentry_non_local(self) -> "Config":
        if self.ENVIRONMENT.is_deployed and not self.SENTRY_DSN:
            raise ValueError("Sentry is not set")

        return self


settings = Config()

print(settings.DATABASE_URL)  # postgresql+asyncpg://usr:pwd@host:5432/db

app_configs: dict[str, Any] = {"title": "App API"}
if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
