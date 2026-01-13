"""
Application configuration using Pydantic settings.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List
from pydantic import field_validator


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application Settings
    APP_NAME: str = "ai-agent-app"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_PORT: int = 8000
    
    # API Keys
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    
    # Windmill Configuration
    WINDMILL_URL: str = "http://localhost:8000"
    WINDMILL_TOKEN: Optional[str] = None
    WINDMILL_WORKSPACE: str = "default"
    
    # Database Configuration
    DATABASE_URL: Optional[str] = None
    REDIS_URL: Optional[str] = None
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    
    # Security
    SECRET_KEY: str = "change-me-in-production"
    JWT_SECRET: str = "change-me-in-production"
    
    # CORS Configuration
    CORS_ORIGINS: str = "*"  # Change for production: use comma-separated URLs
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS origins from comma-separated string to list."""
        if self.CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]
    
    # Agent Configuration
    AGENT_MAX_ITERATIONS: int = 10
    AGENT_TIMEOUT: int = 300
    AGENT_MODEL: str = "gpt-4"
    AGENT_TEMPERATURE: float = 0.7
    
    @field_validator("SECRET_KEY", "JWT_SECRET")
    @classmethod
    def validate_secrets_in_production(cls, v: str, info) -> str:
        """Validate that secret keys are changed in production."""
        # Get the APP_ENV from the values being validated
        app_env = info.data.get("APP_ENV", "development")
        if app_env == "production" and v == "change-me-in-production":
            raise ValueError(
                f"{info.field_name} must be changed from default value in production environment. "
                "Set a secure random value via environment variable."
            )
        return v
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
