#!/usr/bin/env python

import json

with open('file_OFF.json', 'r') as f:
    data = json.load(f)


for el in data:
    for key, value in el.items():
        if key == 'products':
            for el in value:
                for k, v in el.items():
                    if k == 'url':
                        print(k, v)
