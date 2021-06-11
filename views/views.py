# librairies
from colorama import Fore

def menu():
    """Print main menu"""

    print(Fore.LIGHTWHITE_EX + "**Menu**")
    print("[1] Algorithme Force Brute pour 20 actions.")
    print("[3] Algorithme optimisé pour 100 000 actions.")
    print("[0] Quitter le programme.\n")


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
