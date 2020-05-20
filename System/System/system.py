"""File containing core functions."""

from System.Data.aliments import Aliments
from System.Data.categories import Categories
from System.Requests.aliments_req import AlimentsRequests
from System.Requests.categories_req import CategoriesRequests
from System.Requests.db_connection import Base_fn

class System:
    """Core class."""

    def __init__(self, name):
        self.name = name

    def print_menu(self):
        """Display home page."""

        print("--------------- Pur Beurre Technologie. ------------------")
        print("1 >>> Quel aliment souhaitez-vous remplacer?")
        print("2 >>> Retrouver mes aliments substitués.")
        print("3 >>> Réinitialisez la base de donnees.")
        print("4 >>> Quitter le programme.\n")
        choice = input(">>> Tappez le chiffre correspondant au choix voulu. <<<\n")
        return choice

    def exit_pg(self):
        """Leave function."""

        print("-------------------------------------------")
        print("-------------- A Bientot! -----------------")
        print("-------------------------------------------")
        exit()

    def reset_bdd(self):
        """Delete and create the tables."""

        db = Base_fn.create_connection("localhost", "lancelot", "mdp", "OpenFoodFact")
        data = Categories.get_list()
        """---- delete/create bloc ------"""
        CategoriesRequests.del_table(db)
        CategoriesRequests.create_table(db)
        CategoriesRequests.add_data(db, data)
        AlimentsRequests.del_table(db)
        AlimentsRequests.create_table(db)
        """ -----------------------------"""
        list_al = Aliments.get_all(data)
        AlimentsRequests.add_data(db, list_al)
        print("Base de donnee reinitialisee.")

    def print_el_in_list(self, print_list):
        """Print function."""

        print("-------------")
        x = 0
        page = 0
        for element in print_list:
            print(x, ">>>", element)
            if x == 8:
                print("9 >>> Page suivante.")
                choice = input("\n>>> Tappez le chiffre correspondant au choix voulu. <<<\n")
                if int(choice) < 9:
                    result = (int(choice) + (page * 8))
                    return result
                x = 0
                page += 1
            else:
                x += 1
        choice = input("\n>>> Tappez le chiffre correspondant au choix voulu. <<<\n")
        result = (int(choice) + (page * 8))
        return result

    def print_substitution(self, product, sub_list):
        """Print sub detail."""

        print("-----------------")
        print("Produit choisit :", product)
        print("-----------------")
        for element in sub_list:
            print("Substitution possible :", element)


    def select_prod(self):
        """Product choose."""

        db = Base_fn.create_connection("localhost", "lancelot", "mdp", "OpenFoodFact")
        categories_names = CategoriesRequests.get_data(db, "name")
        x = self.print_el_in_list(categories_names)
        category = categories_names[int(x)]
        aliments_in_category = AlimentsRequests.get_aliments_by_category(db, category)
        x = self.print_el_in_list(aliments_in_category)
        substitut = AlimentsRequests.substitute_aliment(db, category)
        self.print_substitution(aliments_in_category[int(x)], substitut)

    def main_loop(self):
        """Core Function."""

        while "infinite":
            x = 0
            while x not in ["1", "3", "4"]:
                x = self.print_menu()
            if x == "1":
                self.select_prod()
            elif x == "3":
                self.reset_bdd()
            elif x == "4":
                self.exit_pg()
