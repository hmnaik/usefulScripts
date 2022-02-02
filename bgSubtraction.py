# This file is to code the automatic subtraction of the background from the images given

import numpy as np
import cv2 as cv


# Read the bg file and generate a background
def generateBackgroundImage( videoCap ):
    # Get first frame as default frame
    ret, firstImage = videoCap.read()
    if ret:
        avgColImage = np.float32(firstImage)
    # Read all the images and make a bgimage
    while(True):
        ret, frame = videoCap.read()
        if ret is False:
            break

        cv.accumulateWeighted(frame, avgColImage, 0.1)
        result = cv.convertScaleAbs(avgColImage)

    print("bg creation over ")

    return result

# Read the video file and do the subtraction
def genSubtractionVideo( fgImage , bgImage):
    fgGray = cv.cvtColor(fgImage,cv.COLOR_BGR2GRAY)
    bgGray = cv.cvtColor(bgImage,cv.COLOR_BGR2GRAY)
    ret, bgGray = cv.threshold(bgGray, 90, 255, cv.THRESH_BINARY)
    ret, fgGray = cv.threshold(fgGray, 90, 255, cv.THRESH_BINARY)
    subImage =   fgGray - bgGray
    #ret, subImage = cv.threshold(subImage,90,255, cv.THRESH_BINARY)

    return subImage



#############
#directory = "D:\\Termites\\bgImage"

bgImage = cv.imread("D:\RealSense Development\RealSenseProjects\device1\\bgImage_scene2.png")
if bgImage is None:
    bgVideo = cv.VideoCapture("D:\RealSense Development\RealSenseProjects\device1\\testColor_device1_pg882_scene2_bg.mp4")
    bgImage = generateBackgroundImage(bgVideo)
    bgVideo.release()
    cv.imwrite("D:\RealSense Development\RealSenseProjects\device1\\bgImage_scene2.png", bgImage)

cv.namedWindow("displaybg", cv.WINDOW_NORMAL)
cv.imshow("displaybg", bgImage)
k = cv.waitKey(0)
if k == 27:
    cv.destroyWindow("displaybg")

# Write code to capture and subtract the video using the background
videoImage = cv.VideoCapture("D:\RealSense Development\RealSenseProjects\device1\\testColor_device1_pg882_scene2.mp4")

while(True):
    ret, frame = videoImage.read()

    if ret: # if there is frame use the function to subtract images
        subImage = genSubtractionVideo(frame, bgImage)
    # Image display options
    cv.namedWindow("subImages", cv.WINDOW_NORMAL)
    cv.imshow("subImages",subImage)

    k = cv.waitKey(10)
    if k == 27:
        cv.destroyAllWindows()
        break

videoImage.release()



