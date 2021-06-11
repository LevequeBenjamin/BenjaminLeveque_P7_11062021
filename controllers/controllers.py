# librairies
from colorama import Fore
import sys

# views
from views import views


def exit_program() -> None:
    """Method used to exit the program."""
    sys.exit()


def main_perform(user_choice: int) -> None:
    """Dispatch the action requested by the user.
    Args:
        user_choice (int): contains the user choice entered by the user.
    """

    commands = {
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
