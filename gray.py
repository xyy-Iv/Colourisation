from glob import glob
import cv2 as cv
import numpy as np
import os
import random

PATH = "/home/yuyang/data/Danbooru/danbooru2017/512px/*"
OUTPUT = "/home/yuyang/data/Danbooru/danbooru2017/gray/"
img_path = glob(PATH)


for f in img_path:
    # print(f)
    if os.path.isdir(f):
        #print(f)
        
        if not os.path.exists(OUTPUT + f.split("/")[-1]):
            os.makedirs(OUTPUT + f.split("/")[-1])
        g = f + "/*.jpg"
        print(g)
        for file in glob(g):
            img = cv.imread(file)

            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

            print(OUTPUT + f.split("/")[-1] + "/" + file.split("/")[-1].split(".")[-2] + "_gray.jpg")
            cv.imwrite( OUTPUT + f.split("/")[-1] + "/"  + file.split("/")[-1].split(".")[-2] + "_gray.jpg", gray)

