
from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    verify_token: str
    page_access_token: str

    class Config:
        env_file = ".env"

settings = Settings()
