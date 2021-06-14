# librairies
from colorama import Fore
import os
import sys


def header() -> None:
    """Header."""
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win32"):
        os.system("cls")
    elif sys.platform.startswith("darwin"):
        os.system("clear")
    print("\n")
    print(Fore.CYAN + "*** -*- ALGOINVEST & TRADE -*- ***".center(119))
    print("\n")
    print("=" * 119)


def menu() -> None:
    """Print main menu."""
    header()
    print(Fore.LIGHTWHITE_EX + "* MENU *".center(119))
    print("\n" * 1)
    print("[1] Algorithme Force Brute pour 20 actions.")
    print("[2] Algorithme glouton pour le fichier dataset1.")
    print("[3] Algorithme glouton pour le fichier dataset2.")
    print("[4] Algorithme optimisé pour le fichier dataset1.")
    print("[5] Algorithme optimisé pour le fichier dataset2.")
    print("[0] Quitter le programme.\n")
    print(Fore.CYAN + "=" * 119)


def prompt_int(message: str) -> int:
    """Prompt for get user choice.

    Args:
        message (str): message for user.

    Returns:
        message (int): user choice.
    """
    try:
        return int(input(message))
    except ValueError:
        print(Fore.LIGHTRED_EX + "Attention ce n'est pas un chiffre.")
        return prompt_int(message)


def prompt_return() -> str:
    """Return Y.
    Returns:
        [type]: [description]
    """
    confirm = ""
    while confirm != "Y":
        confirm = input(
            Fore.LIGHTCYAN_EX + "\n::[Y] pour retourner au menu >> "
        ).upper()
        if confirm not in ["Y", "N"]:
            print(Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire.")
    return confirm


def print_wallet(
    shares: list,
    price: float,
    gain_after_two_years: float,
) -> None:
    """Display a array with information of player dict.
    Args:
        player (dict): a dict of player.
    """
    print(
        f"{'ACTIONS'.center(30)} | "
        f"{'PRIX'.center(30)} | "
        f"{'PROFIT SUR 2 ANS'.center(30)}"
        f"\n{'°' * 119}"
    )
    print(
        f"{str(price).center(30)} | "
        f"{str(gain_after_two_years).center(30)}"
        f"\n{'-' * 119}"
    )
    print("\n".join([share.name for share in shares]))
