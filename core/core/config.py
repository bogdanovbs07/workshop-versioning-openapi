from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    app_title: str = "My API Workshop"
    app_description: str = "API with versioning and OpenAPI client"
    app_version: str = "1.0.0"

    class Config:
        env_file = ".env"

settings = Settings()
