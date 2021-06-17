"""Contains class Wallet."""

# librairies
from typing import List

# models
from models.share import Share


class Wallet:
    """This is a class allowing to create a wallet.

    Attributs:
        shares: list of Share instances.

    Properties:
        price: the total price of shares in the walet.
        gain: the total gain of shares in the wallet.
        gain_after_two_years: the total gain after two years of shares in the wallet.
    """

    def __init__(self, shares: List[Share]) -> None:
        """Inits Wallet.

        Args:
            shares (list): a list of Share instances.
        """
        self.shares = shares

    @property
    def price(self) -> int:
        """The total price of shares in the walet."""
        return sum([share.price / 100 for share in self.shares])

    @property
    def gain(self) -> int:
        """The total gain of shares in the wallet."""
        return sum([share.gain for share in self.shares]) / len(self.shares)

    @property
    def gain_after_two_years(self) -> float:
        """The total gain after two years of shares in the wallet."""
        return round(sum([share.gain_after_two_years for share in self.shares]), 2)
