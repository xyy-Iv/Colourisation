from glob import glob
import cv2 as cv
import numpy as np
import os
import random

img_path = glob("pics/*.jpg")
for file in img_path:
    print(file)
    img = cv.imread(file)
    height, width, c = img.shape

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("a", gray)
    blur = cv.GaussianBlur(gray,(3,3),0)
    cv.imshow("a", blur)
    #cv.waitKey(0)
    #kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (9, 9))
    #dilated = cv.dilate(gray, kernel)
    #cv.imshow("a", dilated)

    #thresh, otsu = cv.threshold(gray, 155, 255, cv.THRESH_BINARY_INV)
    
    #cv.imshow("a", otsu)
    #cv.imwrite(os.path.splitext(file)[0]+str("_otsu.jpg"), otsu)
    #img[otsu == 255] = [0, 0, 255]
    thresh = cv.adaptiveThreshold(blur, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 3)
    #print(ret)
    # max_thresh = 255
    thresh = cv.stylization(thresh, sigma_s=60, sigma_r=0.45)
    #edges = cv.Canny(thresh, 100, 200)
    #edges = ~edges
    cv.imshow("a", thresh)
    cv.imwrite("test" + str(random.random()) + ".jpg", thresh)
    erode = cv.erode(gray, kernel)
    cv.waitKey(0)
    # drawing = np.zeros(img.shape,np.uint8)     # Image to draw the contours
    # _, contours,hierarchy = cv.findContours(edges,cv.RETR_CCOMP,cv.CHAIN_APPROX_SIMPLE)
    # cv.imshow("a", contours)
    # cv.waitKey(0)
    #_, contours, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    #for cnt in contours:
        #hull = cv.convexHull(cnt)
        #cv.drawContours(drawing,[cnt],0,(255,255,),1)   # draw contours in green color
        #cv.drawContours(drawing,[hull],0,(0,0,255),1)  # draw contours in red color
        #cv.imshow('output',drawing)
