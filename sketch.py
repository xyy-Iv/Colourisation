from glob import glob
import cv2 as cv
import numpy as np
import os
import random

img_path = glob("/home/yuyang/data/Danbooru/danbooru2017/512px/0001/*.jpg")

for file in img_path:
    print(file)
    img = cv.imread(file)
    height, width, c = img.shape

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
    cv.imshow("a", thresh)

    cv.imwrite(file.split("/")[-1].split(".")[-2] + "_sketch.jpg", thresh)
    #erode = cv.erode(gray, kernel)
    cv.waitKey(0)
