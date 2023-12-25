from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    database_url: str