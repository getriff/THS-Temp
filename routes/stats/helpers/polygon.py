import requests
import os
from dotenv import load_dotenv
from .data import get_func_distribution, get_top_transactor

load_dotenv()


def get_all_txns(account_address):
    # print(os.environ)
    url = "https://api.polygonscan.com/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&apikey={}".format(
        account_address, os.getenv("POLYSCAN_API")
    )
    # &page=1&offset=10
    headers = {"Content-Type": "application/json"}
    print(url)
    response = requests.request("GET", url, headers=headers)
    # print("response", response)
    func_dist, method_dict = get_func_distribution(response.json()["result"])
    top_t = get_top_transactor(response.json()["result"])
    return {
        "txns": response.json()["result"],
        "total_txns": len(response.json()["result"]),
        "func_dist": func_dist,
        "method_dict": method_dict,
        "top_transactor": top_t,
    }
    # print()


def check_if_verified(contract_address):
    url = "https://api.polygonscan.com/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("POLYSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
    }


def get_all_txns_mum(account_address):
    url = "https://api-testnet.polygonscan.com/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&apikey={}".format(
        account_address, os.getenv("POLYSCAN_API")
    )
    # &page=1&offset=10
    headers = {"Content-Type": "application/json"}

    print(url)

    response = requests.request("GET", url, headers=headers)
    func_dist, method_dict = get_func_distribution(response.json()["result"])
    top_t = get_top_transactor(response.json()["result"])
    return {
        "txns": response.json()["result"],
        "total_txns": len(response.json()["result"]),
        "func_dist": func_dist,
        "method_dict": method_dict,
        "top_transactor": top_t,
    }
    # print()


def check_if_verified_mum(contract_address):
    url = "https://api-testnet.polygonscan.com/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("POLYSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
    }


# testnet polyscan call using requests to fetch abi
def get_abi_mum(contract_addr):
    import requests

    url = "https://api-testnet.polygonscan.com/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_addr, os.getenv("POLYSCAN_API")
    )
    print(url)
    response = requests.get(url)
    return {"verified": response.json()["status"], "abi": response.json()["result"]}


# testnet polyscan call using requests to fetch contract code
def get_code_mum(contract_addr):
    url = "https://api-testnet.polygonscan.com/api?module=contract&action=getsourcecode&address={}&apikey={}".format(
        contract_addr, os.getenv("POLYSCAN_API")
    )
    print(url)
    response = requests.get(url)
    if response.json()["result"][0]["Proxy"] == "1":
        url = "https://api-testnet.polygonscan.com/api?module=contract&action=getsourcecode&address={}&apikey={}".format(
            response.json()["result"][0]["Implementation"], os.getenv("ETHERSCAN_API")
        )
        response2 = requests.get(url)
        abiRet = get_abi_mum(response.json()["result"][0]["Implementation"])
        print(abiRet)
        return {
            "verified": abiRet["verified"],
            "contract_name": response2.json()["result"][0]["ContractName"],
            "code": response2.json()["result"][0]["SourceCode"],
            "abi": abiRet["abi"],
        }

    abiRet = get_abi_mum(contract_addr)
    print(abiRet)
    return {
        "verified": abiRet["verified"],
        "contract_name": response.json()["result"][0]["ContractName"],
        "code": response.json()["result"][0]["SourceCode"],
        "abi": abiRet["abi"],
    }


# get abi function for polygon mainnet
def get_abi(contract_addr, api_key):
    import requests

    url = "https://api.polygonscan.com/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_addr, api_key
    )
    print(url)
    response = requests.get(url)
    return {"verified": response.json()["status"], "abi": response.json()["result"]}


# get contract code function for polygon mainnet
def get_code(contract_addr, api_key):
    url = "https://api.polygonscan.com/api?module=contract&action=getsourcecode&address={}&apikey={}".format(
        contract_addr, api_key
    )
    print(url)
    response = requests.get(url)
    if response.json()["result"][0]["Proxy"] == "1":
        url = "https://api.polygonscan.com/api?module=contract&action=getsourcecode&address={}&apikey={}".format(
            response.json()["result"][0]["Implementation"], os.getenv("ETHERSCAN_API")
        )
        response2 = requests.get(url)
        abiRet = get_abi(response.json()["result"][0]["Implementation"])
        print(abiRet)
        return {
            "verified": abiRet["verified"],
            "contract_name": response2.json()["result"][0]["ContractName"],
            "code": response2.json()["result"][0]["SourceCode"],
            "abi": abiRet["abi"],
        }

    abiRet = get_abi(contract_addr)
    return {
        "verified": abiRet["verified"],
        "contract_name": response.json()["result"][0]["ContractName"],
        "code": response.json()["result"][0]["SourceCode"],
        "abi": abiRet["abi"],
    }
