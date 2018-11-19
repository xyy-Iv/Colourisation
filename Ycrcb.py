from glob import glob
import cv2 as cv
import numpy as np
import os
import random

PATH = "/home/yuyang/data/output/"
OUTPUT = "/home/yuyang/data/a/"
img_path = glob(PATH)

for f in img_path:
    if os.path.isdir(f):
        if not os.path.exists(OUTPUT + f.split("/")[-1]):
            os.makedirs(OUTPUT + f.split("/")[-1])
        g = f + "/*.jpg"
        for file in glob(g):
            print(file)
            img = cv.imread(file)
            gray = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
            gray = np.transpose(np.transpose(gray, (2, 1, 0))[0], (1, 0))
            # cv.imshow("test", gray)
            # cv.waitKey(0)
            print(OUTPUT + file.split("/")[-1])
            cv.imwrite( OUTPUT + file.split("/")[-1], gray, [int(cv.IMWRITE_JPEG_QUALITY), 100])