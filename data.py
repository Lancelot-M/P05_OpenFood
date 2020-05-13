#!/usr/bin/env python

'''File contain data's class.'''

from constantes import CATEGORIES
from data_requests import CategoriesRequests
from db_connection import *
import requests
import json

class Categories:
    '''Data for table categories.'''
    
    def __init__(
        self,
        id_bdd=None,
        name=None,
        url=None,
        products=None):

        self.id_bdd = id_bdd
        self.name = name
        self.url = url
        self.products = products

    def get_categories():
        """Get data from API."""
        data_table = {}
        data_id = 0
        url = "https://fr-en.openfoodfacts.org/categories.json"
        reponse = requests.get(url)
        data = reponse.json()
        for el in data["tags"]:
            if el["name"] in CATEGORIES:
                data_table[data_id] = Categories(id_bdd=data_id, name=el["name"],
                                                    url=el["url"], products=el["products"])
        return data_table


class Aliments:
    """Data for table aliments."""

    def __init__(
        self,
        stores=None,
        nutrition_grades=None,
        product_name=None,
        id_off=None,
        categorie=None):

        self.stores = stores
        self.nutrition_grades = nutrition_grades
        self.product_name = product_name
        self.id_off = id_off

class Saves:
    """Data for table Saves."""

    def __init__(
        self,
        product_chose=None,
        product_substitut=None):

        self.product_chose = product_chose
        self.product_substitute = product_substitut

if __name__ == "__main__":
    
    data = Categories.get_categories()
    CategoriesRequests.del_table(db)
    CategoriesRequestes.create_table(db)

