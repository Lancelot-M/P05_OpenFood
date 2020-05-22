"""File containing core functions."""

from config import HOST, USER, PWD, DATABASE
from System.Data.aliments import Aliments
from System.Data.categories import Categories
from System.Requests.aliments_req import AlimentsRequests
from System.Requests.categories_req import CategoriesRequests
from System.Requests.save_req import SaveRequests
from System.Requests.db_connection import Base_fn

class System:
    """Core class."""

    def __init__(self, connection):
        self.connection = connection

    def launcher():
        """Function to start the app."""
        connection = Base_fn.create_connection(HOST, USER, PWD, DATABASE)
        Ratatouille = System(connection)
        Ratatouille.menu()

    def menu(self):
        """Shunt function."""
        self.print_menu()
        choice = input(">>> Tappez le chiffre correspondant au choix voulu. <<<\n")
        if choice == "1":
            self.select_product()
        elif choice == "2":
            self.show_saving()
        elif choice == "3":
            self.reset_database()
        elif choice == "4":
            self.exit_program()
        else:
            self.menu()

    def print_menu(self):
        """Display home page."""
        print("--------------- Pur Beurre Technologie. ------------------")
        print("1 >>> Quel aliment souhaitez-vous remplacer?")
        print("2 >>> Retrouver mes aliments substitués.")
        print("3 >>> Réinitialisez la base de donnees.")
        print("4 >>> Quitter le programme.\n")

    def exit_program(self):
        """Leave function."""
        print("-------------------------------------------")
        print("-------------- A Bientot! -----------------")
        print("-------------------------------------------")
        exit()

    def reset_database(self):
        """Delete and create the tables."""
        data = Categories.get_list()
        SaveRequests.del_table(self.connection)
        AlimentsRequests.del_table(self.connection)
        CategoriesRequests.del_table(self.connection)
        CategoriesRequests.create_table(self.connection)
        CategoriesRequests.add_data(self.connection, data)
        AlimentsRequests.create_table(self.connection)
        SaveRequests.create_table(self.connection)
        list_al = Aliments.get_all(data)
        AlimentsRequests.add_data(self.connection, list_al)
        print("Base de donnee reinitialisee.")
        self.menu()

    def print_el_in_list(self, print_list):
        """Print function."""
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        line = 0
        page = 0
        choice = 69
        for element in print_list:
            if line == 9:
                print("9 >>> Page suivante.")
                while int(choice) not in range(0, 10):
                    choice = input("\n>>> Tappez le chiffre correspondant au choix voulu. <<<\n")
                if int(choice) in range(0, 9):
                    result = (int(choice) + (page * 8))
                    return result
                else:
                    line = 0
                    page += 1
            else:
                print(line, ">>>", element)
                line += 1
        while int(choice) not in range(0, 9):
            choice = input("\n>>> Tappez le chiffre correspondant au choix voulu. <<<\n")
        result = (int(choice) + (page * 8))
        return result

    def print_substitution(self, product, sub_list):
        """Print sub detail."""
        print("Substitution possibles :")
        item = self.print_el_in_list(sub_list)
        print(">>>>>>---------------------------------<<<<<<")
        print("Vous avez choisi de remplacer", product, "par", sub_list[int(item)][0])
        print(">>>>>>---------------------------------<<<<<<\n")
        data = [product, sub_list[int(item)][0]]
        SaveRequests.add_data(self.connection, data)
        

    def select_product(self):
        """Product choose."""
        categories_names = CategoriesRequests.get_data(self.connection, "name")
        x = self.print_el_in_list(categories_names)
        category = categories_names[int(x)]
        aliments_in_category = AlimentsRequests.get_aliments_by_category(self.connection, category)
        x = self.print_el_in_list(aliments_in_category)
        substitut = AlimentsRequests.substitute_aliment(self.connection, category)
        self.print_substitution(aliments_in_category[int(x)], substitut)
        self.menu()

    def show_saving(self):
        """Show substitute product in database."""
        data = SaveRequests.get_all(self.connection)
        for element in data:
            print(">>> Produit initial:", element[1])
            print(">>> Produit de substitution:", element[1:len(element)], "\n")
        self.menu()
