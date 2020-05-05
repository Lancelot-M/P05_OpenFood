#!/usr/bin/env python

import json
import requests

def check_cat():

    base_url = "https://fr-en.openfoodfacts.org/categories.json"

    reponse = requests.get(base_url)
    data = reponse.json()

    list1 = []
    list2 = ["id", "url", "name", "products"]

    for k, v in data.items():
        if k == "tags":
            for el in v:
                list3 = []
                for k1 in el.keys():
                    if k1 in list2:
                        list3.append(k1)
                if len(list3) == 4:
                    list1.append(el)
    return list1


def check_prod(list_cat):

    fit = ["id", "ingregients_text_fr", "stores", "countries", "product_name", "generic_name","brands", "origins", "product_name_fr", "nutrition_grades", "nutrition_grade_fr", "categories", "categories_hierarchy", ]

    b_url = "https://fr-en.openfoodfacts.org/category/{}.json"
    for el in list_cat[400:420]:
        for k, v in el.items():
            if k == 'name':
                url = b_url.format(v)
                reponse = requests.get(url)
                data = reponse.json()
                print(k, v)
                for k1, v1 in data.items():
                    if k1 == 'products':
                        for el in v1:
                            for key, value in el.items():
                                if key == "product_name":
                                    print(key, ">>>>", value)
                        print("-----------------")
                        print("\n\n")



""" ----------------------------- """


list_cat = check_cat()
check_prod(list_cat)

'''for el in list_cat:
    for k, v in el.items():
        if k == 'name':
            print(k, v)'''



