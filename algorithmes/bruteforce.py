"""Docstrings."""

# librairies
from tqdm import tqdm
from typing import List

# models
from models.share import Share
from models.wallet import Wallet


def brute_force(shares: List[Share], max_price: int) -> List[Wallet]:
    """[summary]

    Args:
        shares (List[Share]): [description]

    Returns:
        List[Wallet]: [description]
    """
    n = len(shares)
    wholes = [i for i in range(2 ** n)]
    binaries = [bin(i)[2:] for i in wholes]
    combinations = ["0" * (n - len(k)) + k for k in binaries]
    selected_shares = []
    valid_combinations = []
    for combi in tqdm(combinations):
        price_combi = 0
        for i in range(n):
            if combi[i] == "1":
                selected_shares.append(shares[i])
                price_combi += shares[i].price
        if price_combi <= max_price and price_combi > 0:
            wallet = Wallet(selected_shares)
            valid_combinations.append(wallet)
        selected_shares = []
    return valid_combinations
