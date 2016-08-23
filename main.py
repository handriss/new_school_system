from models import *
from populator import Populator
from stories import *
import getpass
from collections import OrderedDict


class MainMenu():
    """ Initiates the main menu in the terminal. """
    state = "main"

    def __init__(self):
        Populator.establish_connection()
        Populator.populate_tables()

        self.main_menu = [
            "Applicant's menu",
            "Administrator's menu",
            "Mentor's menu"
            ]

        self.administrator_menu = OrderedDict([
            ("1", ("Story 1: Handle new applications", FirstStory)),
            ("2", ("Story 2: Assign interview slot to applicants", SecondStory)),
            ("3", ("Story 6: Application detail", SixthStory)),
            ("4", ("Story 8: Handle the questions of the applicants", EightStory))
        ])

        self.applicant_menu = OrderedDict([
            ("1", ("Story 3: Application details", ThirdStory)),
            ("2", ("Story 4: Interview Details", FourthStory)),
            ("3", ("Story 5: Check the status of your questions", FifthStory))

        ])

        self.mentor_menu = OrderedDict([
            ("1", ("Story 9: Check scheduled interview", NinthStory))
        ])

        print (" --- WELCOME TO CODECOOL APPLICATION SYSTEM ---")
        print("\nPlease choose from the following options:\n")

        while True:
            if self.state == "main":
                self.call_main_menu()
            elif self.state == "applicant":
                self.applicant()
            elif self.state == "administrator":
                self.administrator()
            elif self.state == "mentor":
                self.mentor()

    def call_main_menu(self):
        """ The main menu, where one can choose from applicant, administrator and mentor submenus. """
        while True:
            for point in self.main_menu:
                print("{0}.: {1}".format(self.main_menu.index(point)+1, point))
            print("\nPress 'x' to exit\n")
            user_input = getpass.getpass(prompt="")

            if user_input == "x":
                exit()
            elif user_input == "1":
                self.state = "applicant"
                return
            elif user_input == "2":
                self.state = "administrator"
                return
            elif user_input == "3":
                self.state = "mentor"
                return

    def applicant(self):
        """ The applicant view submenu. """

        user_input = None
        while user_input != "x":
            for key, value in self.applicant_menu.items():
                print("{}) {}".format(key, value[0]))
            print("\nPress 'x' to exit\n")

            user_input = getpass.getpass(prompt="").lower().strip()
            if user_input in self.applicant_menu:
                self.applicant_menu[user_input][1]()
                user_input = "x"
        self.state = "main"

    def administrator(self):
        """ The administrator view submenu. """

        user_input = None
        while user_input != "x":
            for key, value in self.administrator_menu.items():
                print("{}) {}".format(key, value[0]))
            print("\nPress 'x' to exit\n")

            user_input = getpass.getpass(prompt="")
            if user_input in self.administrator_menu:
                self.administrator_menu[user_input][1]()
        self.state = "main"

    def mentor(self):
        """ The mento view submenu. """

        user_input = None
        while user_input != "x":
            for key, value in self.mentor_menu.items():
                print("{}) {}".format(key, value[0]))
            print("\nPress 'x' to exit\n")

            user_input = getpass.getpass(prompt="")
            if user_input in self.administrator_menu:
                self.mentor_menu[user_input][1]()
        self.state = "main"


def main():
    MainMenu()

if __name__ == "__main__":
    main()
