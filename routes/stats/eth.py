from pyexpat import version_info
from .helpers.eth import (
    check_if_verified_goe,
    get_all_txns,
    check_if_verified,
    get_all_txns_goe,
    get_abi,
    get_contract_code,
    get_abi_goe,
    get_contract_code_goe,
)
from .helpers.data import get_tag, extract_function, compile_prompt
from models.transactions import THSSchema
from web3 import Web3
import json

w3 = Web3()


def eth_health_check(transaction: THSSchema):
    all_txns = get_all_txns(transaction.contractAddress)
    verified = check_if_verified(transaction.contractAddress)
    print(transaction)

    return {
        "total_txns": all_txns["total_txns"],
        "verified": verified["verified"],
        "func_dist": all_txns["func_dist"],
        "method_dist": all_txns["method_dict"],
        "tag": get_tag(int(verified["verified"]), all_txns["total_txns"]),
        "top_transactor": all_txns["top_transactor"],
    }


def goe_eth_health_check(transaction):
    all_txns = get_all_txns_goe(transaction.contractAddress)
    verified = check_if_verified_goe(transaction.contractAddress)
    # print(transaction)
    # print(all_txns)

    return {
        "total_txns": all_txns["total_txns"],
        "verified": verified["verified"],
        "func_dist": all_txns["func_dist"],
        "method_dist": all_txns["method_dict"],
        "tag": get_tag(int(verified["verified"]), all_txns["total_txns"]),
        "top_transactor": all_txns["top_transactor"],
    }


# eth transaction explainer
def eth_transaction_explainer(transaction):

    # get contract code
    code = get_contract_code(transaction.contractAddress)

    if not code["verified"]:
        return {
            "abi": "",
            "code": "",
            "function_code": "",
            "prompt": "",
        }

    # use transaction method

    contract = w3.eth.contract(
        address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        abi=json.loads(code["abi"]),
    )

    # use transaction method

    if transaction.method == "" and transaction.rawTransaction != "":
        transaction.method = (
            str(contract.decode_function_input(transaction.rawTransaction)[0])
            .split(" ")[1]
            .split("(")[0]
            .strip()
        )
    elif transaction.method == "":
        return {
            "abi": code["abi"],
            "code": code["code"],
            "function_code": "",
            "prompt": "",
        }

    print("Here: ", transaction.method)
    try:
        function_code = extract_function(code["code"], transaction.method)

    except Exception as e:
        return {
            "abi": "",
            "code": "",
            "function_code": "",
            "prompt": "",
        }

    # compile prompt
    prompt = compile_prompt(function_code)

    return {
        "abi": code["abi"],
        "code": code["code"],
        "function_code": function_code,
        "prompt": prompt,
    }


# goe eth transaction explainer
def goe_eth_transaction_explainer(transaction):
    # get contract code
    code = get_contract_code_goe(transaction.contractAddress)

    if not code["verified"]:
        return {
            "abi": "",
            "code": "",
            "function_code": "",
            "prompt": "",
        }

    # use transaction method

    print(code["abi"])

    contract = w3.eth.contract(
        address="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        abi=json.loads(code["abi"]),
    )

    # use transaction method

    if transaction.method == "" and transaction.rawTransaction != "":
        transaction.method = (
            str(contract.decode_function_input(transaction.rawTransaction)[0])
            .split(" ")[1]
            .split("(")[0]
            .strip()
        )

    elif transaction.method == "":
        return {
            "abi": code["abi"],
            "code": code["code"],
            "function_code": "",
            "prompt": "",
        }
    print("Here:", transaction.method.strip())
    print("Here:", "Hello")
    try:
        # print(code["code"])
        function_code = extract_function(code["code"], transaction.method)
        print(function_code)
    except Exception as e:
        return {
            "abi": "",
            "code": "",
            "function_code": "",
            "prompt": "",
        }

    # compile prompt
    prompt = compile_prompt(function_code)

    return {
        "abi": code["abi"],
        "code": code["code"],
        "function_code": function_code,
        "prompt": prompt,
    }
