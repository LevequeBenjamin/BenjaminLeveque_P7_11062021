"""Docstrings."""

# librairies
import csv


def get_data(file):
    """[summary]

    Args:
        file ([type]): [description]

    Returns:
        [type]: [description]
    """
    data_shares = []
    with open(file, newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for share in data:
            if float(share["price"]) > 0 and float(share["profit"]) > 0:
                data_shares.append(
                    (
                        share["name"],
                        share["price"],
                        share["profit"],
                    )
                )
    return data_shares
