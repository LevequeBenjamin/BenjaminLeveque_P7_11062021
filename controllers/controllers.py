# librairies
from colorama import Fore
import sys

# models
from models.share import ContructorShare

# algorithmes
from algorithmes.bruteforce import brute_force
from algorithmes.glouton import glouton
from algorithmes.optimized import optimized

# data
from get_data.get_data import get_data

# views
from views import views

# const
SHARES = [
    ("Action-1", 20.00, 5.00),
    ("Action-2", 30.00, 10.00),
    ("Action-3", 50.00, 15.00),
    ("Action-4", 70.00, 20.00),
    ("Action-5", 60.00, 17.00),
    ("Action-6", 80.00, 25.00),
    ("Action-7", 22.00, 7.00),
    ("Action-8", 26.00, 11.00),
    ("Action-9", 48.00, 13.00),
    ("Action-10", 34.00, 27.00),
    ("Action-11", 42.00, 17.00),
    ("Action-12", 110.00, 9.00),
    ("Action-13", 38.00, 23.00),
    ("Action-14", 14.00, 1.00),
    ("Action-15", 18.00, 3.00),
    ("Action-16", 8.00, 8.00),
    ("Action-17", 4.00, 12.00),
    ("Action-18", 10.00, 14.00),
    ("Action-19", 24.00, 21.00),
    ("Action-20", 114.00, 18.00),
]
MAX_PRICE = 50000


def exit_program() -> None:
    """Method used to exit the program."""
    sys.exit()


def brute_force_20():
    shares = ContructorShare.constructor_share(SHARES)
    wallets_brute = brute_force(shares, MAX_PRICE)
    sorted_wallets_brute = sorted(
        wallets_brute, key=lambda wallet: wallet.gain_after_two_years, reverse=True
    )
    views.print_wallet(
        sorted_wallets_brute[0].shares,
        sorted_wallets_brute[0].price,
        sorted_wallets_brute[0].gain_after_two_years,
    )
    #run()


def glouton_data1():
    data_1 = get_data("data/dataset1_Python+P7.csv")
    shares_1 = ContructorShare.constructor_share(data_1)
    sorted_shares_1 = sorted(
        shares_1, key=lambda share: share.gain_after_two_years, reverse=True
    )
    wallet_glouton_1 = glouton(sorted_shares_1, MAX_PRICE)
    for share in wallet_glouton_1.shares:
        print(share.name)
    print(wallet_glouton_1.gain_after_two_years)
    run()


def glouton_data2():
    data_2 = get_data("data/dataset2_Python+P7.csv")
    shares_2 = ContructorShare.constructor_share(data_2)
    sorted_shares_2 = sorted(
        shares_2, key=lambda share: share.gain_after_two_years, reverse=True
    )
    wallet_glouton_2 = glouton(sorted_shares_2, MAX_PRICE)
    for share in wallet_glouton_2.shares:
        print(share.name)
    print(wallet_glouton_2.gain_after_two_years)
    run()


def optimized_data1():
    data_1 = get_data("data/dataset1_Python+P7.csv")
    shares_1 = ContructorShare.constructor_share(data_1)
    wallet_opti = optimized(shares_1, MAX_PRICE)
    print(wallet_opti.price)
    print(wallet_opti.gain)
    print(wallet_opti.gain_after_two_years)
    for share in wallet_opti.shares:
        print(f"name :{share.name}, price:{share.price}, gain:{share.gain}")
    run()


def optimized_data2():
    data_2 = get_data("data/dataset2_Python+P7.csv")
    shares_2 = ContructorShare.constructor_share(data_2)
    wallet_opti_2 = optimized(shares_2, MAX_PRICE)
    print(wallet_opti_2.price)
    print(wallet_opti_2.gain)
    print(wallet_opti_2.gain_after_two_years)
    for share in wallet_opti_2.shares:
        print(f"name :{share.name}, price:{share.price}, gain:{share.gain}")
    run()


def main_perform(user_choice: int) -> None:
    """Dispatch the action requested by the user.
    Args:
        user_choice (int): contains the user choice entered by the user.
    """

    commands = {
        1: brute_force_20,
        2: glouton_data1,
        3: glouton_data2,
        4: optimized_data1,
        5: optimized_data2,
        0: exit_program,
    }
    getattr(commands[user_choice]())

    # # # # # # # # # # # # #
    #    ***** RUN *****    #
    # # # # # # # # # # # # #


def run():
    """Run the programme."""
    views.menu()
    user_choice = 7
    while user_choice not in range(0, 6):
        user_choice = views.prompt_int(
            Fore.LIGHTWHITE_EX + "Que voulez-vous faire ? : "
        )
    main_perform(user_choice)
