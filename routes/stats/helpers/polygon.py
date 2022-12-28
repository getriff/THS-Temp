import requests
import os
from dotenv import load_dotenv
from .data import get_func_distribution

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

    return {
        "txns": response.json()["result"],
        "total_txns": len(response.json()["result"]),
        "func_dist": func_dist,
        "method_dict": method_dict,
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

    return {
        "txns": response.json()["result"],
        "total_txns": len(response.json()["result"]),
        "func_dist": func_dist,
        "method_dict": method_dict,
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
