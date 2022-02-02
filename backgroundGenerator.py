# Read the images from the given directory and display them
import os
from tkinter import filedialog
import cv2 as cv
import numpy as np


#Getting the user to select the path
rootPath = filedialog.askdirectory()

bgPathCol = rootPath + "/bgColor.jpg"
bgPathDepth = rootPath + "/bgDepth.jpg"

colorImgPath = rootPath + "/color"
depthImgPath = rootPath + "/depth"
# Gathering images from directory
colorIm = []
for filepath, dir, files in os.walk(colorImgPath):#'D:\Visual Studio Projects\kinectInterface\Images\color'):
    for i in files:
        colorIm.append(os.path.join(filepath,i))

depthIm = []
for filepath, dir, files in os.walk(depthImgPath):#'D:\Visual Studio Projects\kinectInterface\Images\depth'):
    for i in files:
        depthIm.append(os.path.join(filepath,i))

counter = 0

col = cv.imread(colorIm[counter])
dep = cv.imread(depthIm[counter])
avg1col = np.float32(col)
avg1dep = np.float32(dep)

while(counter != len(colorIm) ):

    colImg = cv.imread(colorIm[counter])
    depImg = cv.imread(depthIm[counter])

    cv.accumulateWeighted(colImg,avg1col,0.1)
    cv.accumulateWeighted(depImg,avg1dep,0.1)

    res1 = cv.convertScaleAbs(avg1col)
    res2 = cv.convertScaleAbs(avg1dep)

    cv.namedWindow('avg1',cv.WINDOW_NORMAL)
    cv.namedWindow('avg2', cv.WINDOW_NORMAL)
    cv.imshow('avg1', res1)
    cv.imshow('avg2', res2)


    counter += 1
    k = cv.waitKey(10)
    if(counter == len(colorIm)):
        cv.waitKey(0)

    if k == 27:
        break
    elif k == ord('a') and counter != 0:
        counter -= 1
        continue
    elif k == ord('s'):
        counter += 1
        continue
    else:
        print("Invalid Key Entry : %d" %counter)

# When everything done, release the capture
cv.imwrite(bgPathCol, res1)
cv.imwrite(bgPathDepth, res2)
cv.destroyAllWindows()