from pydantic import BaseSettings
from starlette.config import Config


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8080


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)


config = Config("src/.env")

DATABASE_URL = config("DATABASE_URL", cast=str, default="")
