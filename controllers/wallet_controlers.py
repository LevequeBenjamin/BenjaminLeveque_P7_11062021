"""Docstrings."""

# librairies
from tqdm import tqdm
from operator import itemgetter

from models.share import Share, ContructorShare
from models.wallet import Wallet

# const
SHARES = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ("Action-3", 50, 15),
    ("Action-4", 70, 17),
    ("Action-5", 60, 17),
    ("Action-6", 80, 25),
    ("Action-7", 22, 7),
    ("Action-8", 26, 11),
    ("Action-9", 48, 13),
    ("Action-10", 34, 27),
    ("Action-11", 42, 17),
    ("Action-12", 110, 9),
    ("Action-13", 38, 23),
    ("Action-14", 14, 1),
    ("Action-15", 18, 3),
    ("Action-16", 8, 8),
    ("Action-17", 4, 12),
    ("Action-18", 10, 14),
    ("Action-19", 24, 21),
    ("Action-20", 114, 18),
]
MAX_PRICE = 500


def test():
    shares = ContructorShare.constructor_share(SHARES)
    wallets = brute_force_backpack(shares)
    sorted_wallet = sorted(
        wallets, key=lambda wallet: wallet.gain_after_two_years, reverse=True
    )
    print(sorted_wallet[0].shares)


def glutton_backpack(max_price, shares, selected_shares=[]):
    i = 0
    total_price = 0
    while i < len(shares) and total_price < max_price:
        share = shares[i]
        if total_price + share.price <= max_price:
            selected_shares.append(share)
            total_price += share.price
        i += 1
    return (total_price, selected_shares)


def brute_force_backpack(shares):
    n = len(shares)
    wholes = [i for i in range(2 ** n)]
    binaries = [bin(i)[2:] for i in wholes]
    combinations = ["0" * (n - len(k)) + k for k in binaries]
    selected_shares = []
    valid_combinations = []
    for combi in combinations:
        price_combi = 0
        for i in range(n):
            if combi[i] == "1":
                selected_shares.append(shares[i])
                price_combi += shares[i].price
        if price_combi <= MAX_PRICE:
            wallet = Wallet(price_combi, selected_shares)
            valid_combinations.append(wallet)
        selected_shares = []
    return valid_combinations
