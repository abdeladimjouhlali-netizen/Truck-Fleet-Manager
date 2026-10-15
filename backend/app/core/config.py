from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://localhost:27017"
    SECRET: str = "SUPER_SECRET"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()
