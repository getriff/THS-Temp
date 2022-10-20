import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_all_txns(account_address):
    url = "https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&apikey={}".format(
        account_address, os.getenv("Etherscan_API")
    )
    # &page=1&offset=10
    headers = {"Content-Type": "application/json"}

    print(url)

    response = requests.request("GET", url, headers=headers)

    return {"txns": response.json(), "total_txns": len(response.json()["result"])}
    # print()


def check_if_verified(contract_address):
    url = "https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("Etherscan_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
    }


def get_all_txns_goe(account_address):
    url = "https://api-goerli.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&apikey={}".format(
        account_address, os.getenv("Etherscan_API")
    )
    # &page=1&offset=10
    headers = {"Content-Type": "application/json"}

    print(url)

    response = requests.request("GET", url, headers=headers)

    return {"txns": response.json(), "total_txns": len(response.json()["result"])}
    # print()


def check_if_verified_goe(contract_address):
    url = "https://api-goerli.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(
        contract_address, os.getenv("Etherscan_API")
    )
    headers = {"Content-Type": "application/json"}

    print(url)
    response = requests.request("GET", url, headers=headers)
    return {
        "verified": response.json()["status"],
    }
