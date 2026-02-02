from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "app"
    db_name: str | None = None
    db_password: str | None = None
    db_user: str | None = None
    db_address: str | None = None
    db_port: str | None = None
    debug: bool = False

    model_config = {
        "env_file": ".env",           # Обязательно!
        "env_file_encoding": "utf-8"   # Для кириллицы и др. символов
    }


settings = Settings()