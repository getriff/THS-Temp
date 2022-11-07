from pyexpat import version_info
from .helpers.eth import (
    check_if_verified_goe,
    get_all_txns,
    check_if_verified,
    get_all_txns_goe,
)
from .helpers.data import get_tag
from models.transactions import THSSchema


def eth_health_check(transaction: THSSchema):
    all_txns = get_all_txns(transaction.contractAddress)
    verified = check_if_verified(transaction.contractAddress)
    print(transaction)

    return {
        "total_txns": all_txns["total_txns"],
        "verified": verified["verified"],
        "func_dist": all_txns["func_dist"],
        "tag": get_tag(verified["verified"], all_txns["total_txns"]),
    }


def goe_eth_health_check(transaction):
    all_txns = get_all_txns_goe(transaction.contractAddress)
    verified = check_if_verified_goe(transaction.contractAddress)
    print(transaction)

    return {
        "total_txns": all_txns["total_txns"],
        "verified": verified["verified"],
        "func_dist": all_txns["func_dist"],
        "tag": get_tag(verified["verified"], all_txns["total_txns"]),
    }
