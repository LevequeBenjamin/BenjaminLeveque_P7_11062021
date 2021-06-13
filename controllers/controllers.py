# librairies
from colorama import Fore
import sys

# controllers
from controllers.bruteforce_controllers import get_wallets_500
from controllers.optimized_controllers import test

# views
from views import views


def exit_program() -> None:
    """Method used to exit the program."""
    sys.exit()


def brute_force_controllers():
    get_wallets_500()
    run()


def main_perform(user_choice: int) -> None:
    """Dispatch the action requested by the user.
    Args:
        user_choice (int): contains the user choice entered by the user.
    """

    commands = {
        3: test,
        1: brute_force_controllers,
        0: exit_program,
    }
    getattr(commands[user_choice]())

    # # # # # # # # # # # # #
    #    ***** RUN *****    #
    # # # # # # # # # # # # #


def run():
    """Run the programme."""
    views.menu()
    user_choice = views.prompt_int(Fore.LIGHTWHITE_EX + "Que voulez-vous faire ? : ")
    main_perform(user_choice)
