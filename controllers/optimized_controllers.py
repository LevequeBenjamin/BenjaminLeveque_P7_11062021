# librairies
import csv
from tqdm import tqdm

# models
from models.share import ContructorShare
from models.wallet import Wallet

MAX_PRICE = 500


def test():

    data_1 = get_data("data/dataset1_Python+P7.csv")
    data_2 = get_data("data/dataset2_Python+P7.csv")
    shares_1 = ContructorShare.constructor_share(data_1)
    shares_2 = ContructorShare.constructor_share(data_2)
    # sorted_shares_1 = sorted(shares_1, key=lambda share: share.gain, reverse=True)
    # sorted_shares_2 = sorted(shares_2, key=lambda share: share.gain, reverse=True)
    # wallet_1 = glouton_backpack(sorted_shares_1)
    # wallet_2 = glouton_backpack(sorted_shares_2)
    wallet_opti = optimized_backpack(shares_1, MAX_PRICE * 100)
    wallet = Wallet(wallet_opti)
    print(wallet.gain_after_two_years)
    # print(wallet_1.gain_after_two_years)
    # print(wallet_2.gain_after_two_years)
    # for share in wallet.shares:
    #     print(share.name)
    # print(wallet.price)
    # print(wallet.gain_after_two_years)


def get_data(file):
    data_shares = []
    with open(file, newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for share in data:
            data_shares.append(
                (share["name"], float(share["price"]), float(share["profit"]))
            )
    return data_shares


def glouton_backpack(shares, selected_shares=[]):
    i = 0
    total_price = 0
    while i < len(shares) and total_price <= MAX_PRICE:
        share = shares[i]
        if total_price + share.price <= MAX_PRICE:
            selected_shares.append(share)
            total_price += share.price
        i += 1
    wallet = Wallet(total_price, selected_shares)
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
