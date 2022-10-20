from hmac import trans_5C
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from models.api import ResponseModel, ErrorResponseModel
from models.transactions import THSSchema
from .stats.eth import eth_health_check, goe_eth_health_check
from .stats.polygon import mum_poly_health_check, poly_health_check

router = APIRouter()


@router.post(
    "/",
    response_description="Gives transaction health statistics for input transaction details",
)
async def get_tx_health(transaction: THSSchema = Body(...)):
    """
    Algorithm:
        - Check if contract owner is in blacklist or not (Stat #1)
        - Check if contract is verified or not (Stat #2)
        - Fetch all Txns and get total number of txns. (Make Scoring Stat) (Stat #3)
        - Aggregate on methods, get distribution, see which is most popular. Is it payable/not? (Stat #4)
        - ERC20 Tokens In and Out (Stat $5)
    """
    if transaction.networkId == 1:
        response = eth_health_check(transaction)
    elif transaction.networkId == 5:
        response = goe_eth_health_check(transaction)
    elif transaction.networkId == 137:
        response = poly_health_check(transaction)
    elif transaction.networkId == 80001:
        response = mum_poly_health_check(transaction)
    else:
        return ErrorResponseModel(
            "Network not implemented",
            404,
            "Network ID {} has not been implemented".format(transaction.networkId),
        )
    return ResponseModel(response, "Transaction Health Stats")
