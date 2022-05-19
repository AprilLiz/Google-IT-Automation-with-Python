#!/usr/bin/env python3
from PIL import Image
import os

cwd = os.getcwd()
src_dir = cwd + '/supplier-data/images/'

images = os.listdir(src_dir)


def image_editor():
    """Converts images from TIFF to JPEG"""
    for image in images:
        if image.endswith('.tiff'):
            img = Image.open(src_dir + image)
            # Use the image name without the .tiff extension
            image_name = image[:-5]
            img.convert('RGB').resize((600, 400)).save(src_dir + image_name + '.jpeg', 'JPEG')
            img.close()


image_editor()
