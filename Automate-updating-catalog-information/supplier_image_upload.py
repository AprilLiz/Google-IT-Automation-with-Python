#!/usr/bin/env python3
import requests
import os

URL = "http://localhost/upload/"
cwd = os.getcwd()
src_dir = cwd + "/supplier-data/images/"

images = os.listdir(src_dir)

# Upload images from the source directory to the URL website
for image in images:
    if image.endswith('.jpeg'):
        with open(os.path.join(src_dir, image), 'rb') as opened:
            r = requests.post(URL, files={'file': opened})
