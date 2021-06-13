"""Docstrings."""

# librairies
from tqdm import tqdm

from models.share import ContructorShare
from models.wallet import Wallet

# const
SHARES = [
    ("Action-1", 20.0, 5.0),
    ("Action-2", 30.0, 10.0),
    ("Action-3", 50.0, 15.0),
    ("Action-4", 70.0, 20.0),
    ("Action-5", 60.0, 17.0),
    ("Action-6", 80.0, 25.0),
    ("Action-7", 22.0, 7.0),
    ("Action-8", 26.0, 11.0),
    ("Action-9", 48.0, 13.0),
    ("Action-10", 34.0, 27.0),
    ("Action-11", 42.0, 17.0),
    ("Action-12", 110.0, 9.0),
    ("Action-13", 38.0, 23.0),
    ("Action-14", 14.0, 1.0),
    ("Action-15", 18.0, 3.0),
    ("Action-16", 8.0, 8.0),
    ("Action-17", 4.0, 12.0),
    ("Action-18", 10.0, 14.0),
    ("Action-19", 24.0, 21.0),
    ("Action-20", 114.0, 18.0),
]
SHARES_TEST = [
    ("Action-1", 2, 5),
    ("Action-2", 3, 10),
    ("Action-3", 5, 15),
    ("Action-4", 7, 20),
]
MAX_PRICE = 500


def get_wallets_500():
    shares = ContructorShare.constructor_share(SHARES)
    wallet_optimized = optimized_backpack(shares, MAX_PRICE)
    wallet = Wallet(wallet_optimized)
    print(wallet.price)
    print(wallet.gain_after_two_years)

    wallets_brute = brute_force_backpack(shares)
    sorted_wallets_brute = sorted(
        wallets_brute, key=lambda wallet: wallet.gain_after_two_years, reverse=True
    )
    for share in sorted_wallets_brute[0].shares:
        print(share.name)
    print(sorted_wallets_brute[0].price)
    print(sorted_wallets_brute[0].gain_after_two_years)

    wallet_glouton = glouton_backpack(shares)
    print(wallet_glouton.price)
    print(wallet_glouton.gain_after_two_years)

    # wallet_glouton = glouton_backpack(shares)
    # wallets = brute_force_backpack(shares)
    # sorted_wallet = sorted(
    #     wallets, key=lambda wallet: wallet.gain_after_two_years, reverse=True
    # )
    # for share in sorted_wallet[0].shares:
    #     print(share.name)
    # print(
    #     sorted_wallet[0].gain_after_two_years,
    #     sorted_wallet[0].price,
    # )
    # print(wallet_glouton.gain_after_two_years)
    # print(sorted_wallet[-1].shares, sorted_wallet[-1].gain_after_two_years)
    # print(len(wallets))


def brute_force_backpack(shares):
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
        if price_combi <= MAX_PRICE and price_combi > 0:
            wallet = Wallet(selected_shares)
            valid_combinations.append(wallet)
        selected_shares = []
    return valid_combinations


def glouton_backpack(shares, selected_shares=[]):
    i = 0
    total_price = 0
    while i < len(shares) and total_price <= MAX_PRICE:
        share = shares[i]
        if total_price + share.price <= MAX_PRICE:
            selected_shares.append(share)
            total_price += share.price
        i += 1
    wallet = Wallet(selected_shares)
    return wallet


def optimized_backpack(shares, max_price):
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
    return selected_shares
