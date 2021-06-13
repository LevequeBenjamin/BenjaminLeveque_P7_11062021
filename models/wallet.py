"""Contains class Share"""

from tqdm import tqdm
from operator import itemgetter

"""[summary]

Returns:
    [type]: [description]
"""


class Wallet:
    """[summary]"""

    def __init__(self, shares: list, MAX_PRICE: int = 500) -> None:
        """[summary]

        Args:
            shares (list): [description]
        """
        # self.price = price
        self.shares = shares
        self.MAX_PRICE = MAX_PRICE

    @property
    def price(self):
        return sum([share.price for share in self.shares])

    @property
    def gain(self):
        return sum([share.gain for share in self.shares]) / len(self.shares)

    @property
    def gain_after_two_years(self):
        return round((self.price * self.gain) / 100, 2)

    def sorted_shares(self) -> list:
        sorted_shares = sorted(self.shares, key=lambda share: share.gain, reverse=True)
        return sorted_shares
