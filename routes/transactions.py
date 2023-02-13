from hmac import trans_5C
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from models.api import ResponseModel, ErrorResponseModel
from models.transactions import THSSchema, THSExplain
import openai

from .stats.eth import (
    eth_health_check,
    goe_eth_health_check,
    eth_transaction_explainer,
    goe_eth_transaction_explainer,
)
from .stats.polygon import (
    mum_poly_health_check,
    poly_health_check,
    polygon_transaction_explainer,
    polygon_testnet_transaction_explainer,
)

router = APIRouter()

openai.api_key = "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"


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


@router.post(
    "/explain/",
    response_description="Gives an explaination of what the transaction does at the blockchain level",
)
async def get_tx_explain(transaction: THSExplain = Body(...)):
    """
    Algorithm:
        - Check if contract is verified by fecthing the source code and ABI
        - If its not verified, return a generic text
        - If its verified and Source code is available, decode Txn
        - Create a prompt and call the open ai api
        - Extract explaination from the response and return it
    """
    if transaction.networkId == 1:
        explainer_meta = eth_transaction_explainer(transaction)
        # print(explainer_meta)
        if explainer_meta["prompt"] == "":
            return ErrorResponseModel(
                "Method not found",
                404,
                "method {} not found".format(transaction.method),
            )
        response = openai.Edit.create(
            model="code-davinci-edit-001",
            input=explainer_meta["prompt"],
            instruction="Replace [insert] with correct answer to the question",
            temperature=0,
            top_p=1,
        )
        response = response.choices[0].text.split("\n \n A.")[1]

    elif transaction.networkId == 5:
        explainer_meta = goe_eth_transaction_explainer(transaction)
        # print(explainer_meta)
        if explainer_meta["prompt"] == "":
            return ErrorResponseModel(
                "Method not found",
                404,
                "method {} not found".format(transaction.method),
            )
        response = openai.Edit.create(
            model="code-davinci-edit-001",
            input=explainer_meta["prompt"],
            instruction="Replace [insert] with correct answer to the question",
            temperature=0,
            top_p=1,
        )
        response = response.choices[0].text.split("\n \n A.")[1]
    elif transaction.networkId == 137:
        explainer_meta = polygon_transaction_explainer(transaction)
        # print(explainer_meta)
        if explainer_meta["prompt"] == "":
            return ErrorResponseModel(
                "Method not found",
                404,
                "method {} not found".format(transaction.method),
            )

        response = openai.Edit.create(
            model="code-davinci-edit-001",
            input=explainer_meta["prompt"],
            instruction="Replace [insert] with correct answer to the question",
            temperature=0,
            top_p=1,
        )
        response = response.choices[0].text.split("\n \n A.")[1]
    elif transaction.networkId == 80001:
        explainer_meta = polygon_testnet_transaction_explainer(transaction)

        # print(explainer_meta)
        if explainer_meta["prompt"] == "":
            return ErrorResponseModel(
                "Method not found",
                404,
                "method {} not found".format(transaction.method),
            )

        response = openai.Edit.create(
            model="code-davinci-edit-001",
            input=explainer_meta["prompt"],
            instruction="Replace [insert] with correct answer to the question",
            temperature=0,
            top_p=1,
        )
        # print(response.choices[0].text)

        response = response.choices[0].text.split("\n \n A.")[1]
    else:
        return ErrorResponseModel(
            "Network not implemented",
            404,
            "Network ID {} has not been implemented".format(transaction.networkId),
        )
    return ResponseModel(response, "Transaction Explaination")
