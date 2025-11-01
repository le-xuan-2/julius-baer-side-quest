"""
Minimal banking client implementation using requests.
"""
from typing import Optional
import requests
from .config import config
from .models import TransferRequest, TransferResponse
from .exceptions import APIError, ValidationError
from .logger import get_logger

logger = get_logger(__name__)


class BankingClient:
    def __init__(self, base_url: str = config.API_BASE_URL, timeout: int = config.API_TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def transfer(self, from_account: str, to_account: str, amount: float, auth_token: Optional[str] = None) -> TransferResponse:
        # Validate input using Pydantic model
        try:
            req = TransferRequest(fromAccount=from_account, toAccount=to_account, amount=amount)
        except Exception as e:
            logger.error("Validation failed: %s", e)
            raise ValidationError(str(e)) from e

        url = f"{self.base_url}/transfer"
        headers = {"Content-Type": "application/json"}
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"

        try:
            resp = self.session.post(url, json=req.model_dump(), headers=headers, timeout=self.timeout)
            if resp.status_code != 200:
                raise APIError(f"API returned {resp.status_code}", status_code=resp.status_code, response=resp.text)
            data = resp.json()
            return TransferResponse(**data)
        except requests.RequestException as e:
            logger.error("Request failed: %s", e)
            raise APIError(str(e)) from e

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
