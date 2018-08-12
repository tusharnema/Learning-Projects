#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
import os
import sys
import glob

path = '/Users/tusharnema/Desktop/opencv/google-images-deep-learning/images/taylor'
dirs = os.listdir(path)
save = '/Users/tusharnema/Desktop/opencv/google-images-deep-learning/images/new-taylor'

import glob

imagePaths = [f for f in glob.glob(os.path.join(path,'*.jpg'))]  # or .png, .tif, etc

def resize():
    for item in imagePaths:
        im = Image.open(item)
        im = im.convert('RGB')
        f = os.path.basename(item)
        imResize = im.resize((200, 200), Image.ANTIALIAS)
        imResize.save(os.path.join(save,f), 'JPEG', quality=90)


resize()
