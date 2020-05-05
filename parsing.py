#!/usr/bin/env python

import json
import requests

url = "https://fr-en.openfoodfacts.org/category/Plant-based  beverages.json"

"--------------------------------------------------------------------------"

XXX = ["id", "ingregients_text_fr", "stores", "countries", "product_name", "generic_name","brands", "origins", "product_name_fr", "nutrition_grades", "nutrition_grade_fr"]

cat_keys = ['id', 'known', 'url', 'name', 'products', 'sameAs']


#reponse = requests.get(url)
#data = reponse.json()
#print(json.dumps(data, indent=4))


def check_categories(b_url):
    url = b_url.format("categories")
    lis = []

    reponse = requests.get(url)
    data = reponse.json()
    for k, v in data.items():
        if k == "tags":
            for el in v:
                T = el["name"]
                if T.find(":") == -1:
                    lis.append(T)
    return(lis)

"------------------------------------------------------------------------------------"

def check_product(url):
        
        reponse = requests.get(url)
        data = reponse.json()
        for k, v in data.items():
            if k == "products":
                for el in v:
                    for k2, v2 in el.items():
                        print(k2)
                    print("--------------")

"-----------------------------------------------------------"
check_product(url)
