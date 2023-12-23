from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str


settings = Settings(_env_file=".env")