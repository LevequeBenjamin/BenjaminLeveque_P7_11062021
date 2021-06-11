"""Contains class Share"""

from tqdm import tqdm
from operator import itemgetter

"""[summary]

Returns:
    [type]: [description]
"""


class Wallet:
    """[summary]"""

    def __init__(self, shares: list):
        """[summary]

        Args:
            shares (list): [description]
        """
        self.shares = shares
        self.share = []
        self.all_shares = []
        self.MAX_PRICE = 500

    def sorted_shares(self) -> list:
        sorted_shares = sorted(self.shares, key=lambda share: share.gain, reverse=True)
        return sorted_shares

    def wallet_500(self):
        pass

    def knapsack(self):
        shares_one = self.wallet_500()
        #sorted_all_best_action = sorted(shares_one, key=itemgetter(-1), reverse=True)
        #return sorted_all_best_action
