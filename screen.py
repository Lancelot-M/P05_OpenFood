#!/usr/bin/env python

"""Interaction with terminal file."""

from data_requests import CategoriesRequests, AlimentsRequests
from db_connection import *
from data import Categories, Aliments
from constantes import MAX_PROD

class Program:
    """Display object."""

    def __init__(self, name):
        self.name = name

    def print_menu(self):
        """Show the home page."""

        print("--------------- Pur Beurre Technologie. ------------------")
        print("Tappez: ")
        print("1 >>> Choisir un produit.")
        print("2 >>> Consulter mes selections.")
        print("3 >>> Réinitialisez la base de donnees")
        print("4 >>> Quitter le programme.")

    def exit_pg(self):
        """Leave function."""

        print("A Bientot! o7")
        exit()

    def reset_bdd(self):
        """Delete and Create the database."""

        db = Base_fn.create_connection("localhost", "lancelot", "mdp", "OpenFoodFact")
        data = Categories.get_list()
        #delete/create table bloc
        CategoriesRequests.del_table(db)
        CategoriesRequests.create_table(db)
        CategoriesRequests.add_data(db, data)
        AlimentsRequests.del_table(db)
        AlimentsRequests.create_table(db)
        list_al = Aliments.get_all(data)
        AlimentsRequests.add_data(db, list_al)
        print("Base de donnee reinitialisee.")

    def select_prod(self):
        """Product choose."""

        db = Base_fn.create_connection("localhost", "lancelot", "mdp", "OpenFoodFact")
        categories_names = CategoriesRequests.get_data(db, "name")
        x = 0
        for element in categories_names:
            print(x, ">>>", element)
            x += 1
        print("")
        x = input(">>> Choisissez une categorie en tappant le chiffre correspondant. <<<\n")
        category = categories_names[int(x)]
        aliments_in_category = AlimentsRequests.get_aliments_by_category(db, category)
        x = 0
        for element in aliments_in_category:
            print(x, ">>>", element)
            x += 1
        print('')
        x = input(">>> Choisissez un produit en tappant le chiffre correspondant. <<<\n")
        substitut = AlimentsRequests.substitute_aliment(db, category)
        for element in substitut:
            print("Produit:", aliments_in_category[int(x)], "// Substitution:", element)

    def main_loop(self):
        """Core Function."""

        x = 0
        while x not in ["1", "3", "4"]:
            self.print_menu()
            x = input()
        if x == "1":
            self.select_prod()
        elif x == "3":
            self.reset_bdd()
        elif x == "4":
            self.exit_pg()


if __name__ == "__main__":


    ratatouille = Program("rasta")
    ratatouille.main_loop()
