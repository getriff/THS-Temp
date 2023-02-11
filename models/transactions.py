from typing import Optional
from pydantic import BaseModel, SecretStr, Field


class THSSchema(BaseModel):
    networkId: int = Field(...)
    networkName: str = Field(...)
    contractAddress: str = Field(...)
    method: str = Field(...)
    methodId: str = Field(...)
    stateMutability: str = Field(...)
    rawTransaction: str = Field(...)

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


class THSExplain(BaseModel):
    networkId: int = Field(...)
    networkName: str = Field(...)
    contractAddress: str = Field(...)
    method: str = Field(...)
    stateMutability: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "networkId": 80001,
                "networkName": "Polygon Mumbai Testnet",
                "contractAddress": "0x51bf3a760A5083a73BD80bea5Da4f702D48c4946",
                "method": "resellToken",
                "methodId": "0x77ad1892",
                "stateMutability": "nonpayable",
                "raxTransaction": "0xf8a0018504a817c80082520894a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48080b84477ad189280000000",
            }
        }
