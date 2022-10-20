from typing import Optional
from pydantic import BaseModel, SecretStr, Field


class THSSchema(BaseModel):
    networkId: int = Field(...)
    networkName: str = Field(...)
    contractAddress: str = Field(...)
    method: str = Field(...)
    stateMutability: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "networkId": 1,
                "networkName": "Ethereum",
                "contractAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "method": "transfer",
                "stateMutability": "nonpayable",
            }
        }
