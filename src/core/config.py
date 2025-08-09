from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
