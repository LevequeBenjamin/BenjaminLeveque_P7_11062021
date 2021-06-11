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
        nb_shares,
        max_cost,
        gain_after_two_year_by_shares,
        gain_with_500,
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
        self.nb_shares = nb_shares
        self.max_cost = max_cost
        self.gain_after_two_year_by_shares = gain_after_two_year_by_shares
        self.gain_with_500 = gain_with_500


class ContructorShare:
    @staticmethod
    def constructor_share(shares):
        new_shares = []
        for share in shares:
            nb_shares = int(500 / share[1])
            max_cost = round((nb_shares * share[1]), 2)
            gain_after_two_year_by_shares = (share[1] / 100) * (share[2])
            gain_with_500 = round((nb_shares * gain_after_two_year_by_shares), 2)
            new_share = Share(
                share[0],
                share[1],
                share[2],
                nb_shares,
                max_cost,
                gain_after_two_year_by_shares,
                gain_with_500,
            )
            new_shares.append(new_share)
        return new_shares
