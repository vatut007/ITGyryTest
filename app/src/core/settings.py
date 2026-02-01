from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name = "app"


settings = Settings()
