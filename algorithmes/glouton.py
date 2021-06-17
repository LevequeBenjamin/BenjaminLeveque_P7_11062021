"""Contains the glutton algorithm."""

# librairies
from typing import List

# models
from models.share import Share
from models.wallet import Wallet


def glouton(shares: List[Share], max_price: int) -> Wallet:
    """Glutton algorithm.

    Args:
        shares (List[Share]): a list of Share intance.
        max_price (int): a max price of wallet.

    Returns:
        Wallet: a Wallet instance.
    """
    selected_shares = []
    i = 0
    total_price = 0
    while i < len(shares) and total_price <= max_price:
        share = shares[i]
        if total_price + share.price <= max_price:
            selected_shares.append(share)
            total_price += share.price
        i += 1
    return Wallet(selected_shares)
