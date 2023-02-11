from pyexpat import version_info
from .helpers.polygon import (
    check_if_verified_mum,
    get_all_txns,
    check_if_verified,
    get_all_txns_mum,
    get_abi,
    get_code,
    get_abi_mum,
    get_code_mum,
)
from .helpers.data import get_tag, extract_function, compile_prompt
from models.transactions import THSSchema


def poly_health_check(transaction: THSSchema):
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


def mum_poly_health_check(transaction):
    all_txns = get_all_txns_mum(transaction.contractAddress)
    verified = check_if_verified_mum(transaction.contractAddress)
    print(transaction)

    return {
        "total_txns": all_txns["total_txns"],
        "verified": verified["verified"],
        "func_dist": all_txns["func_dist"],
        "method_dist": all_txns["method_dict"],
        "tag": get_tag(int(verified["verified"]), all_txns["total_txns"]),
        "top_transactor": all_txns["top_transactor"],
    }


# polygon transaction explainer
def polygon_transaction_explainer(transaction):
    # get abi
    abi = get_abi(transaction.contractAddress)
    # get contract code
    code = get_code(transaction.contractAddress)

    # TODO: abi decodin txn or checking method id later

    # use transaction method

    if transaction.method == "":
        return {
            "abi": abi["abi"],
            "code": code["code"],
            "function_code": "",
            "prompt": "",
        }

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
        "abi": abi["abi"],
        "code": code["code"],
        "function_code": function_code,
        "prompt": prompt,
    }


# polygon testnet transaction explainer
def polygon_testnet_transaction_explainer(transaction):
    # get abi
    abi = get_abi_mum(transaction.contractAddress)

    # get contract code
    code = get_code_mum(transaction.contractAddress)

    # TODO: abi decodin txn or checking method id later

    # use transaction method

    # print(transaction.method)

    if transaction.method == "":
        return {
            "abi": abi["abi"],
            "code": code["code"],
            "function_code": "",
            "prompt": "",
        }

    try:
        function_code = extract_function(code["code"], transaction.method)
    except Exception as e:
        return {
            "abi": "",
            "code": "",
            "function_code": "",
            "prompt": "",
        }

    # print(function_code)

    # compile prompt
    prompt = compile_prompt(function_code)

    return {
        "abi": abi["abi"],
        "code": code["code"],
        "function_code": function_code,
        "prompt": prompt,
    }
