"""File contain class Categories."""

import requests
from System.System.constants import CATEGORIES


class Categories:
    """Class representative of categories's data."""

    def __init__(self, id_bdd=None, name=None,
                 url=None, products=None):
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
                data_table[el["name"]] = Categories(id_bdd=data_id,
                                                    name=el["name"],
                                                    url=el["url"],
                                                    products=el["products"])
                data_id += 1
        return data_table
