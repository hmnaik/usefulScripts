# Read the images from the given directory and display them
import os
from tkinter import filedialog
import cv2 as cv
import numpy as np

def showImage(windowName,src):
    cv.namedWindow(windowName,cv.WINDOW_NORMAL)
    cv.imshow(windowName,src)


#Getting the user to select the path
rootPath = filedialog.askdirectory()
colorImgPath = rootPath + "/color"
depthImgPath = rootPath + "/depth"
bgPathCol = rootPath + "/bgColor.jpg"
bgPathDepth = rootPath + "/bgDepth.jpg"


if os.path.isfile(bgPathCol) and os.path.isfile(bgPathDepth):
    bgColorImg = cv.imread(bgPathCol)
    showImage("background Color", bgColorImg)
    bgDepthImg = cv.imread(bgPathDepth)
    showImage("background Depth", bgDepthImg)
else:
    print("No background images available")
    quit()

# Gathering images from directorysssssssssss
colorImList = []
for filepath, dir, files in os.walk(colorImgPath):#'D:\Visual Studio Projects\kinectInterface\Images\color'):
    for i in files:
        colorImList.append(os.path.join(filepath,i))

depthImList = []
for filepath, dir, files in os.walk(depthImgPath):#'D:\Visual Studio Projects\kinectInterface\Images\depth'):
    for i in files:
        depthImList.append(os.path.join(filepath,i))

counter = 0

while( counter != len(colorImList) ):

    # Get color Image
    colImg = cv.imread(colorImList[counter])
    showImage("Color",colImg)
    # Subtract color Image
    subtractedCol = colImg.copy() #Making deep copy
    cv.subtract(colImg,bgColorImg,subtractedCol) # src, bg, output
    showImage("SubColor", subtractedCol)

    # Get depth Image
    depthImg = cv.imread(depthImList[counter])
    showImage("Depth", depthImg)
    # Subtract color Image
    subtractedDep = depthImg.copy()
    cv.subtract(depthImg,bgDepthImg,subtractedDep)
    showImage("SubDepth", subtractedDep)

    # Show diff in color map
    colorMapDep = subtractedDep.copy() # Deep copy
    cv.applyColorMap(subtractedDep, cv.COLORMAP_JET,colorMapDep)
    showImage("SubDepthColmap", colorMapDep)

    # Print Information
    print(counter)
    k = cv.waitKey(0)
    if k == ord('a') and counter != 0:
        counter -= 1
        continue
    elif k == ord('s'):
        counter += 1
        continue
    elif k == 27:
        cv.destroyAllWindows()
        break
    else:
        print("Invalid Key Entry : %d" %counter)

# When everything done, release the capture
cv.destroyAllWindows()