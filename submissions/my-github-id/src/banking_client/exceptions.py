"""
Banking Client - Custom Exceptions
Copied from provided template
"""

class BankingClientException(Exception):
    """Base exception for all banking client errors."""
    pass


class ConfigurationError(BankingClientException):
    """Raised when configuration is invalid or missing."""
    pass


class AuthenticationError(BankingClientException):
    """Raised when authentication fails."""
    pass


class TransferError(BankingClientException):
    """Raised when transfer operation fails."""
    pass


class ValidationError(BankingClientException):
    """Raised when input validation fails."""
    pass


class APIError(BankingClientException):
    """Raised when API communication fails."""

    def __init__(self, message: str, status_code: int | None = None, response: dict | None = None):
        self.status_code = status_code
        self.response = response
        super().__init__(message)


class AccountValidationError(BankingClientException):
    """Raised when account validation fails."""
    pass


class InsufficientFundsError(TransferError):
    """Raised when account has insufficient funds for transfer."""

    def __init__(self, message: str, requested: float, available: float, shortfall: float):
        self.requested = requested
        self.available = available
        self.shortfall = shortfall
        super().__init__(message)
