"""
Banking Client - Configuration Module
Copied and adapted from provided template
"""

from pathlib import Path
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables from .env file located at project root (if present)
project_root = Path(__file__).resolve().parents[3]
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)


class Config:
    """Application configuration management."""

    # API Configuration
    API_BASE_URL: str = os.getenv("API_BASE_URL", "http://localhost:8123")
    API_TIMEOUT: int = int(os.getenv("API_TIMEOUT", "30"))

    # Authentication
    AUTH_USERNAME: str = os.getenv("AUTH_USERNAME", "alice")
    AUTH_PASSWORD: str = os.getenv("AUTH_PASSWORD", "password")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Transfer Defaults
    DEFAULT_TRANSFER_AMOUNT: float = float(os.getenv("DEFAULT_TRANSFER_AMOUNT", "100.0"))

    @classmethod
    def validate(cls) -> bool:
        """Validate configuration is correctly set up."""
        required_fields = ["API_BASE_URL"]
        for field in required_fields:
            if not getattr(cls, field, None):
                return False
        return True

    @classmethod
    def to_dict(cls) -> dict:
        """Export configuration as dictionary."""
        return {
            key: getattr(cls, key)
            for key in dir(cls)
            if not key.startswith("_") and key.isupper()
        }


# Export for easy import
config = Config()
