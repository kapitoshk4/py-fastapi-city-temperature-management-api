from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Fastapi city temperature management api"

    DATABASE_URL: str | None = "sqlite+aiosqlite:///./city_temperature_management.db"

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = Settings()
url = "https://api.weatherapi.com/v1/current.json"
