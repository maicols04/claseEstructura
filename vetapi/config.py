import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # API Settings
    app_name: str = "Client-Pet API"
    api_version: str = "v1"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # Database Settings
    db_user: str = "root"
    db_password: str = "password"
    db_host: str = "localhost"
    db_port: str = "3306"
    db_name: str = "mydatabase"

    class Config:
        env_file = ".env"

settings = Settings()
