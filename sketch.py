from glob import glob
import cv2 as cv
import numpy as np
import os
import random

PATH = "/home/yuyang/data/Danbooru/danbooru2017/512px/*"
OUTPUT = "/home/yuyang/data/Danbooru/danbooru2017/sketch/"
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
            #print(file)
            img = cv.imread(file)
            # height, width, c = img.shape

            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            #img = two_pass(gray)
            #cv.imshow("a", img)
            blur = cv.GaussianBlur(gray,(3,3),0)
            #blur = nonMaximalSupress1(~blur, [3, 3])

            kernel = np.ones((3, 3),np.uint8)
            thresh = cv.dilate(blur, kernel)
            thresh = cv.adaptiveThreshold(thresh, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 2)
            #thresh,th3=cv.threshold(thresh,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
            #thresh = ~thresh
                
            #erosion = cv2.erode(img,kernel,iterations = 1)
            #thresh = cv.dilate(thresh, kernel)
            #thresh = nonMaximalSupress1(thresh, [3, 3])
            #thresh = cv.Canny(thresh, 100, 200)
            #cv.imshow("a", thresh)
            print(OUTPUT + f.split("/")[-1] + "/" + file.split("/")[-1].split(".")[-2] + "_sketch.jpg")
            cv.imwrite( OUTPUT + f.split("/")[-1] + "/"  + file.split("/")[-1].split(".")[-2] + "_sketch.jpg", thresh)
            #erode = cv.erode(gray, kernel)
            #cv.waitKey(0)
