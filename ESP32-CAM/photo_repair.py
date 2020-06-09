import os
import cv2
import shutil
from os import listdir
from os.path import isfile, join

basedir = os.path.abspath(os.getcwd())

onlyfiles = [f for f in listdir(basedir) if isfile(join(basedir, f))]
new_folder = "numerated" 

for idx, filename in enumerate(onlyfiles):   
    base, extension = os.path.splitext(filename)
    if extension == ".jpg":
        print(filename)
        img = cv2.imread(filename)
        cv2.imwrite(filename, img)