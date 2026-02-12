from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # This will look for an environment variable named OPENAI_API_KEY
    openai_api_key: str = "your-placeholder-key"

    class Config:
        env_file = ".env"

settings = Settings()