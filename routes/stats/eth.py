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
    print(transaction)
    print(all_txns)

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
    # get abi
    abi = get_abi(transaction.contractAddress)
    # get contract code
    code = get_contract_code(transaction.contractAddress)

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


# goe eth transaction explainer
def goe_eth_transaction_explainer(transaction):
    # get abi
    abi = get_abi_goe(transaction.contractAddress)
    # get contract code
    code = get_contract_code_goe(transaction.contractAddress)

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
