import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    openai_api_key = os.getenv("OPENAI_API_KEY", "sk-test-key")
    database_url = os.getenv("DATABASE_URL", "postgresql://localhost/atsight")
    jwt_secret = os.getenv("JWT_SECRET", "test-secret")
    jwt_algorithm = os.getenv("JWT_ALGORITHM", "HS256")
    environment = os.getenv("ENVIRONMENT", "development")

settings = Settings()
