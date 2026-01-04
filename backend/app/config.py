from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    database_url: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    environment: str = "development"
    
    class Config:
        env_file = ".env"


settings = Settings()
