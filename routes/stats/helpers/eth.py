import requests
import os
from dotenv import load_dotenv
from .data import get_func_distribution, get_top_transactor

load_dotenv()


def get_all_txns(account_address):
    url = "https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&apikey={}".format(
        account_address, os.getenv("ETHERSCAN_API")
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


def check_if_verified(contract_address):
    url = "https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("ETHERSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
        "abi": response.json()["result"],
    }


def get_all_txns_goe(account_address):
    url = "https://api-goerli.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&apikey={}".format(
        account_address, os.getenv("ETHERSCAN_API")
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


def check_if_verified_goe(contract_address):
    url = "https://api-goerli.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("ETHERSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
        "abi": response.json()["result"],
    }


# get abi function for eth mainnet
def get_abi(contract_address):
    url = "https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("ETHERSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
        "abi": response.json()["result"],
    }


# get contract code function for eth mainnet
def get_contract_code(contract_address):
    url = "https://api.etherscan.io/api?module=proxy&action=eth_getCode&address={}&tag=latest&apikey={}".format(
        contract_address, os.getenv("ETHERSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
        "contract_name": response.json()["result"][0]["ContractName"],
        "code": response.json()["result"][0]["SourceCode"],
    }


# get abi function for goerli testnet
def get_abi_goe(contract_address):
    url = "https://api-goerli.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("ETHERSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
        "abi": response.json()["result"],
    }


# get contract code function for goerli testnet
def get_contract_code_goe(contract_address):
    url = "https://api-goerli.etherscan.io/api?module=proxy&action=eth_getCode&address={}&tag=latest&apikey={}".format(
        contract_address, os.getenv("ETHERSCAN_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
        "contract_name": response.json()["result"][0]["ContractName"],
        "code": response.json()["result"][0]["SourceCode"],
    }
