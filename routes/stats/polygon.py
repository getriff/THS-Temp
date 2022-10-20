from pyexpat import version_info
from .helpers.polygon import (
    check_if_verified_mum,
    get_all_txns,
    check_if_verified,
    get_all_txns_mum,
)
from models.transactions import THSSchema


def poly_health_check(transaction: THSSchema):
    all_txns = get_all_txns(transaction.contractAddress)
    verified = check_if_verified(transaction.contractAddress)
    print(transaction)

    return {
        "total_txns": all_txns["total_txns"],
        "verified": verified["verified"],
    }


def mum_poly_health_check(transaction):
    all_txns = get_all_txns_mum(transaction.contractAddress)
    verified = check_if_verified_mum(transaction.contractAddress)
    print(transaction)

    return {
        "total_txns": all_txns["total_txns"],
        "verified": verified["verified"],
    }
