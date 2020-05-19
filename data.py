#!/usr/bin/env python

'''File contain data's class.'''

from constantes import CATEGORIES
from data_requests import CategoriesRequests
from data_requests import AlimentsRequests
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

    def get_list():
        """Get data from API."""
        data_table = {}
        data_id = 0
        url = "https://fr-en.openfoodfacts.org/categories.json"
        reponse = requests.get(url)
        data = reponse.json()
        for el in data["tags"]:
            if el["name"] in CATEGORIES:
                data_table[el["name"]] = Categories(id_bdd=data_id, name=el["name"],
                                                    url=el["url"], products=el["products"])
                data_id += 1
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
        self.categorie = categorie

    def get_all(dict_categorie):
        """Get all aliments from each categorie."""

        list_all = []
        aliments_by_categorie = {}
        b_url = "https://fr-en.openfoodfacts.org/category/{}.json"
        for key in dict_categorie.keys():
            url = b_url.format(key)
            reponse = requests.get(url)
            data = reponse.json()
            clean_list = Aliments.filter_key(data)
            aliments_by_categorie[key] = clean_list
        
        for key, value in aliments_by_categorie.items():
            for element_dict in value:
                if "stores" in element_dict.keys():
                    list_all.append(Aliments(stores=element_dict["stores"],nutrition_grades=element_dict["nutrition_grades"], product_name=element_dict["product_name"], id_off=element_dict["id"], categorie=key))
                else:
                    list_all.append(Aliments(nutrition_grades=element_dict["nutrition_grades"], product_name=element_dict["product_name"], id_off=element_dict["id"], categorie=key))
        return list_all

    def filter_key(dict_of_categorie):
        """Check keys in dict."""

        check = ["nutrition_grades", "product_name", "categories"]
        clean_list = []
        for element in dict_of_categorie["products"]:
            if all(el in element.keys() for el in check):
                clean_list.append(element)
        return clean_list
                

class Saves:
    """Data for table Saves."""

    def __init__(
        self,
        product_chose=None,
        product_substitut=None):

        self.product_chose = product_chose
        self.product_substitute = product_substitut

if __name__ == "__main__":
   
    db = Base_fn.create_connection("localhost", "lancelot", "mdp", "OpenFoodFact") 
    """
    data = Categories.get_list()
    CategoriesRequests.del_table(db)
    CategoriesRequests.create_table(db)
    CategoriesRequests.add_data(db, data)
    AlimentsRequests.del_table(db)
    AlimentsRequests.create_table(db)
    list_al = Aliments.get_all(data)
    AlimentsRequests.add_data(db, list_al)
    data = AlimentsRequests.get_name(db)
    """
    data = AlimentsRequests.get_aliments_by_category(db, 'Hams')
    print(data)

