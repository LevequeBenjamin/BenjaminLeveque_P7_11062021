"""Docstrings."""

# librairies
from tqdm import tqdm
from typing import List

# models
from models.share import Share
from models.wallet import Wallet


def optimized(shares: List[Share], max_price: int) -> Wallet:
    """[summary]

    Args:
        shares ([type]): [description]
        max_price ([type]): [description]

    Returns:
        [type]: [description]
    """
    matrice = [[0 for x in range(max_price + 1)] for x in range(len(shares) + 1)]
    for i in tqdm(range(1, len(shares) + 1)):
        for p in range(1, max_price + 1):
            if shares[i - 1].price <= p:
                matrice[i][p] = max(
                    shares[i - 1].gain_after_two_years
                    + matrice[i - 1][p - shares[i - 1].price],
                    matrice[i - 1][p],
                )
            else:
                matrice[i][p] = matrice[i - 1][p]

    p = max_price
    n = len(shares)
    selected_shares = []

    while p >= 0 and n >= 0:
        e = shares[n - 1]
        if matrice[n][p] == matrice[n - 1][p - e.price] + e.gain_after_two_years:
            selected_shares.append(e)
            p -= e.price

        n -= 1
    return Wallet(selected_shares)
