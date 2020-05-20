"""File containing aliments class."""

import json
import requests

class Aliments:
    """Class representative of aliments's data."""

    def __init__(
        self,
        stores=None,
        nutrition_grades=None,
        product_name=None,
        id_off=None,
        categorie=None,
        url=None):

        self.stores = stores
        self.nutrition_grades = nutrition_grades
        self.product_name = product_name
        self.id_off = id_off
        self.categorie = categorie
        self.url = url

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
                    list_all.append(Aliments(url=element_dict["product_name"], id_off=element_dict["id"], categorie=key))
                else:
                    list_all.append(Aliments(url=element_dict["url"], nutrition_grades=element_dict["nutrition_grades"], product_name=element_dict["product_name"], id_off=element_dict["id"], categorie=key))
        return list_all

    def filter_key(dict_of_categorie):
        """Check keys in dict."""

        check = ["nutrition_grades", "product_nae", "categories", "url"]
        clean_list = []
        for element in dict_of_categorie["products"]:
            if all(el in element.keys() for el in check):
                clean_list.apend(element)
        check = []
        for element in clean_list:
            if len(element["product_name"]) < 4:
                check.append(element)
        clean_list = [element for element in clean_list if element not in check]
        return clean_list
