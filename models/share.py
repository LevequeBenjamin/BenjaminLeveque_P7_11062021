"""Contains class Share"""


"""[summary]

Returns:
    [type]: [description]
"""


class Share:
    """[summary]"""

    def __init__(
        self,
        name,
        price,
        gain,
    ):
        """[summary]

        Args:
            name ([type]): [description]
            price ([type]): [description]
            gain ([type]): [description]
        """
        self.name = name
        self.price = price
        self.gain = gain
        self.rapport = gain / price

    def __str__(self):
        return self.name, self.price

    def get_tuple(self) -> tuple:
        return (self.name, self.price, self.gain)

    @property
    def gain_after_two_years(self):
        return ((self.price / 100) * (self.gain)) / 100


class ContructorShare:
    @staticmethod
    def constructor_share(shares):
        new_shares = []
        for i in range(len(shares)):
            new_shares.append(
                Share(
                    shares[i][0],
                    int(float(shares[i][1]) * 100),
                    float(shares[i][2]),
                )
            )
        return new_shares
