"""Contains the brute force algorithm."""

# librairies
from typing import List
from tqdm import tqdm

# models
from models.share import Share
from models.wallet import Wallet


def brute_force(shares: List[Share], max_price: int) -> List[Wallet]:
    """Brute force algorithm.

    Args:
        shares (List[Share]): a list of Share instance.
        max_price (int): a max price of wallet.

    Returns:
        List[Wallet]: a list of Wallet instance.
    """
    len_shares = len(shares)
    wholes = list(i for i in range(2 ** len_shares))
    binaries = list(bin(i)[2:] for i in wholes)
    combinations = list("0" * (len_shares - len(k)) + k for k in binaries)
    selected_shares = []
    valid_combinations = []
    for combi in tqdm(combinations):
        price_combi = 0
        for i in range(len_shares):
            if combi[i] == "1":
                selected_shares.append(shares[i])
                price_combi += shares[i].price
        if max_price >= price_combi > 0:
            wallet = Wallet(selected_shares)
            valid_combinations.append(wallet)
        selected_shares = []
    return valid_combinations
