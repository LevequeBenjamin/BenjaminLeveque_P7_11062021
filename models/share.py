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

    @property
    def gain_after_two_years(self):
        return (self.price / 100) * (self.gain)


class ContructorShare:
    @staticmethod
    def constructor_share(shares):
        new_shares = []
        for share in shares:
            new_share = Share(
                share[0],
                share[1],
                share[2],
            )
            new_shares.append(new_share)
        return new_shares
