"""Contains get_data function."""

# librairies
import csv


def get_data(file: str) -> list:
    """Function that allows you to read a csv file.

    Args:
        file (string): the path of the csv file.

    Returns:
        list (str): a list of information retrieved in the csv file.
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
