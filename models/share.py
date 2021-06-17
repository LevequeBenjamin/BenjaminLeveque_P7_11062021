"""Contains class Share"""


class Share:
    """This is a class allowing to create a share.

    Attributs:
        name: a name of share.
        price: a price of share.
        gain: a gain of share.

    Properties:
        gain_after_two_years: the total gain after two years of share.
    """

    def __init__(
        self,
        name: int,
        price: int,
        gain: float,
    ) -> None:
        """[summary]

        Args:
            name (str): a name of share.
            price (int): a price of share.
            gain (float): a gain of share.
        """
        self.name = name
        self.price = price
        self.gain = gain

    @property
    def gain_after_two_years(self) -> None:
        """The total gain after two years of share."""
        return ((self.price / 100) * (self.gain)) / 100


class ContructorShare:
    """This is a class allowing to create a share instance.

    Methods:
        static constructor_share(shares):
    """

    @staticmethod
    def constructor_share(shares: list) -> list:
        """Allows you to build Share instances.

        Args:
            shares (list): a list of share.

        Returns:
            new_shares (list(Share)): a list of Share instances.
        """
        new_shares = []
        for i in range(int(len(shares))):
            new_shares.append(
                Share(
                    shares[i][0],
                    int(float(shares[i][1]) * 100),
                    float(shares[i][2]),
                )
            )
        return new_shares
