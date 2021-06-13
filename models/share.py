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

    def get_tuple(self) -> tuple:
        return (self.name, self.price, self.gain)

    @property
    def gain_after_two_years(self):
        return int((self.price / 100) * (self.gain))


class ContructorShare:
    @staticmethod
    def constructor_share(shares):
        new_shares = []
        for share in shares:
            if share[1] > 0 and share[2] > 0:
                new_share = Share(
                    share[0],
                    share[1],
                    share[2],
                )
                new_shares.append(new_share)
        return new_shares
