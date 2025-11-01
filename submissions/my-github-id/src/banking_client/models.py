"""
Pydantic models for banking client
Minimal versions to get started
"""
from pydantic import BaseModel, Field, field_validator


class TransferRequest(BaseModel):
    fromAccount: str = Field(..., regex=r"^ACC\d{4}$")
    toAccount: str = Field(..., regex=r"^ACC\d{4}$")
    amount: float = Field(..., gt=0)


class TransferResponse(BaseModel):
    transactionId: str
    status: str
    message: str
    fromAccount: str
    toAccount: str
    amount: float
    availableBalance: float | None = None
    requestedAmount: float | None = None
    shortfall: float | None = None
