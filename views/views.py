"""Contains the main view."""

# librairies
import os
import sys
from colorama import Fore


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
        confirm (str): user choice.
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
    """Display a array with information of wallet.

    Args:
        shares (list(Shares)): a list of Share instances.
        price (float): a total price of wallet.
        gain_after_two_years (float): a gain after two years of wallet.
    """
    print(f"{'ACTIONS'.center(40)} | " f"\n{'°' * 42}")
    print("\n".join([share.name for share in shares]))
    print(f"{'-' * 42}")
    print(f"{'PRIX'.center(20)}|" f"{'PROFIT SUR 2 ANS'.center(20)}|" f"\n{'°' * 42}")
    print(
        Fore.LIGHTRED_EX + f"{str(price).center(20)}" + Fore.LIGHTWHITE_EX + "|"
        f"{Fore.LIGHTGREEN_EX + str(gain_after_two_years).center(20)}"
        + Fore.LIGHTWHITE_EX
        + "|"
        f"\n{Fore.LIGHTWHITE_EX + '-' * 42}"
    )
