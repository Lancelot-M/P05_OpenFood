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
        """Function to start the application."""
        connection = Base_fn.create_connection(HOST, USER, PWD, DATABASE)
        system = System(connection)
        system.menu()

    def menu(self):
        """Shunt function."""
        self.print_menu()
        choice = input(">>> Tapez le chiffre correspondant "
                       "a la ligne a selectionner. <<<\n")
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
        print("\n", "-" * 20, "Pur Beurre Application.", "-" * 20)
        print("1 >>> Trouver un aliment de substitution")
        print("2 >>> Retrouver mes aliments substitues.")
        print("3 >>> Reinitialisez la base de donnees.")
        print("4 >>> Quitter le programme.")
        print("-" * 60)

    def exit_program(self):
        """Leave function."""
        print("-" * 60)
        print("-" * 23, " A Bientot! ", "-" * 23)
        print("-" * 60)
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

    def print_pages(self, print_list):
        """Print list 8 elements by 8."""
        line = 0
        page = 0
        check_list = []
        choice = None
        print("-" * 88)
        for el in range(0, 10):
            check_list.append(str(el))
        for element in print_list:
            print(line, ">>>", element)
            line += 1
            if line == 9:
                print("9 >>> Page suivante.")
                print("-" * 88)
                while choice not in check_list:
                    choice = input(">>> Tapez le chiffre correspondant"
                                   " a la ligne a selectionner. <<<\n")
                if choice != "9":
                    result = (int(choice) + (page * 8))
                    return result
                else:
                    line = 0
                    page += 1
                    print("-" * 88)
        print("-" * 88)
        while choice not in check_list[0:8]:
            choice = input(">>> Tapez le chiffre correspondant"
                           " a la ligne a selectionner. <<<\n")
        result = (int(choice) + (page * 8))
        return result

    def print_substitution(self, product, sub_list):
        """Print choosing detail."""
        choice = None
        print("-" * 88)
        print("Substitutions possibles ci dessous.")
        item = self.print_pages(sub_list)
        print(">" * 6, "-" * 80, "<" * 6)
        print("Vous avez choisi de remplacer", product, "par",
              sub_list[int(item)][0])
        print(">" * 6, "-" * 80, "<" * 6)
        while True:
            print("Voulez vous sauvegarder ce resultat?")
            print("0 >>> Oui")
            print("1 >>> Non")
            choice = input(">>> Tapez le chiffre correspondant"
                           " a la ligne a selectionner. <<<\n")
            if choice == "0":
                data = [product, sub_list[int(item)][0]]
                SaveRequests.add_data(self.connection, data)
                print("Resultat sauvegarde.")
                break
            elif choice == "1":
                break

    def select_product(self):
        """Selection product process."""
        categories_names = CategoriesRequests.get_data(self.connection, "name")
        number = self.print_pages(categories_names)
        category = categories_names[number]
        aliments_in_category = AlimentsRequests.get_aliments_by_category(
                self.connection, category)
        number = self.print_pages(aliments_in_category)
        substitut = AlimentsRequests.substitute_aliment(self.connection,
                                                        category)
        self.print_substitution(aliments_in_category[number], substitut)
        self.menu()

    def show_saving(self):
        """Show substitute product in database."""
        data = SaveRequests.get_all(self.connection)
        print("-" * 88)
        print("-" * 40, "SAVING", "-" * 40)
        print("-" * 88)
        for element in data:
            print(">>> Produit initial:", element[1])
            print(">>> Produit de substitution:",
                  element[1:len(element)])
            print("-" * 80)
        self.menu()
