"""Docstrings."""

# librairies
from tqdm import tqdm
from operator import itemgetter

from models.share import Share, ContructorShare
from models.wallet import Wallet

# const
SHARES = [
    ["Action-1", 20, 5],
    ["Action-2", 30, 10],
    ["Action-3", 50, 15],
    ["Action-4", 70, 17],
    ["Action-5", 60, 17],
    ["Action-6", 80, 25],
    ["Action-7", 22, 7],
    ["Action-8", 26, 11],
    ["Action-9", 48, 13],
    ["Action-10", 34, 27],
    ["Action-11", 42, 17],
    ["Action-12", 110, 9],
    ["Action-13", 38, 23],
    ["Action-14", 14, 1],
    ["Action-15", 18, 3],
    ["Action-16", 8, 8],
    ["Action-17", 4, 12],
    ["Action-18", 10, 14],
    ["Action-19", 24, 21],
    ["Action-20", 114, 18],
]
MAX_PRICE = 500


# def sorted_shares() -> list:
#     """Function which allows to calculate and return
#     a list in the order of the most interesting action to the least

#     Returns:
#         sorted_shares (list): [description]
#     """
#     shares = []
#     best_shares = []
#     for share in SHARES:
#         nb_shares = int(MAX_PRICE / share[1])
#         max_cost = nb_shares * share[1]
#         gain_after_two_year_by_shares = (share[1] / 100) * (share[2])
#         gain_with_500 = nb_shares * gain_after_two_year_by_shares
#         shares += share
#         shares.append(round(max_cost, 2))
#         shares.append(round(gain_with_500, 2))
#         shares.append(nb_shares)
#         best_shares.append(shares)
#         shares = []

#     sorted_shares = sorted(best_shares, key=itemgetter(2), reverse=True)
#     return sorted_shares


def test():
    shares = ContructorShare.constructor_share(SHARES)
    wallet = Wallet(shares)
    sorted_all_best_action = wallet.knapsack()
    #print(sorted_all_best_action)
    #print(len(sorted_all_best_action))


test()
