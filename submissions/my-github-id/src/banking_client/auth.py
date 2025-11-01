"""
Simple JWT authenticator stub.
"""
from typing import Optional
import requests
from .config import config
from .exceptions import AuthenticationError
from .logger import get_logger

logger = get_logger(__name__)


class JWTAuthenticator:
    def __init__(self, base_url: str = config.API_BASE_URL):
        self.base_url = base_url
        self.token: Optional[str] = None

    def get_token(self, scope: str = "transfer") -> str:
        try:
            url = f"{self.base_url}/authToken"
            resp = requests.post(url, json={"scope": scope}, timeout=config.API_TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            self.token = data.get("token")
            if not self.token:
                raise AuthenticationError("No token in response")
            return self.token
        except requests.RequestException as e:
            logger.error("Authentication request failed: %s", e)
            raise AuthenticationError(str(e)) from e
