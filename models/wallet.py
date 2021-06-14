"""Contains class Share"""


"""[summary]

Returns:
    [type]: [description]
"""


class Wallet:
    """[summary]"""

    def __init__(self, shares: list) -> None:
        """[summary]

        Args:
            shares (list): [description]
        """
        # self.price = price
        self.shares = shares
        # self.MAX_PRICE = MAX_PRICE

    @property
    def price(self) -> int:
        """[summary]

        Returns:
            [type]: [description]
        """
        return sum([share.price / 100 for share in self.shares])

    @property
    def gain(self) -> int:
        """[summary]

        Returns:
            [type]: [description]
        """
        return sum([share.gain for share in self.shares]) / len(self.shares)

    @property
    def gain_after_two_years(self) -> float:
        """[summary]

        Returns:
            [type]: [description]
        """
        return round(
            sum([share.gain_after_two_years for share in self.shares]), 2
        )
