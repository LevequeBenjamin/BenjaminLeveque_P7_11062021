"""Contains the optimized algorithm."""

# librairies
from typing import List
from tqdm import tqdm

# models
from models.share import Share
from models.wallet import Wallet


def optimized(shares: List[Share], max_price: int) -> Wallet:
    """Optimized algorithm.

    Args:
        shares (list[Share]): a list of Share instance.
        max_price (int): a max price of wallet.

    Returns:
        Wallet: a Wallet instance.
    """
    matrice = list([0 for x in range(max_price + 1)] for x in range(len(shares) + 1))
    for i in tqdm(range(1, len(shares) + 1)):
        for len_price in range(1, max_price + 1):
            if shares[i - 1].price <= len_price:
                matrice[i][len_price] = max(
                    shares[i - 1].gain_after_two_years
                    + matrice[i - 1][len_price - shares[i - 1].price],
                    matrice[i - 1][len_price],
                )
            else:
                matrice[i][len_price] = matrice[i - 1][len_price]

    len_price = max_price
    len_shares = len(shares)
    selected_shares = []

    while len_price >= 0 and len_shares >= 0:
        share = shares[len_shares - 1]
        if (
            matrice[len_shares][len_price]
            == matrice[len_shares - 1][len_price - share.price]
            + share.gain_after_two_years
        ):
            selected_shares.append(share)
            len_price -= share.price

        len_shares -= 1
    return Wallet(selected_shares)
