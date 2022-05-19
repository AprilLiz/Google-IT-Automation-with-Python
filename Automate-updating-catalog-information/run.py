#! /usr/bin/env python3
import os
import requests

cwd = os.getcwd()
path = cwd + '/supplier-data/descriptions/'
URL = "http://localhost/fruits/"

files = os.listdir(path)

# Convert data from parsed .txt files to json format and upload it to the URL website
for file in files:
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        fruit_dict = {'name': lines[0],
                      'weight': int(lines[1][:-5]),
                      'description': lines[2],
                      'image_name': file.split(".")[0] + ".jpeg"}
        response = requests.post(URL, json=fruit_dict)
        # If uploading status code is error, raise exception
        response.raise_for_status()
        print(response.status_code)
