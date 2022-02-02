
import cv2
import numpy as np
import os

def converttoGrayImage( image ):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def siftFeature(image):
    sift = cv2.xfeatures2d.SIFT_create()
    kp, desc = sift.detectAndCompute(image, None)
    return kp,desc

def drawsiftKeyPoints( grayImage, colorImage, kp):
    out = cv2.drawKeypoints(grayImage, colorImage.clone() , kp)
    return out


# Read Images Stack
file = "D:\\testVideos\\VID_20190516_192528094.mp4"
if os.path.exists(file):
    print("Video Exists")
else:
    exit()

cap = cv2.VideoCapture(file)
# Read Template Images
#tempImage = cv2.imread("D:\Yolo Detection\\temp2.jpg")
ret, tempImage = cap.read()
gray1 = converttoGrayImage(tempImage)
kptempImage1, kptempImage1Feat = siftFeature(gray1)



counter = 0

while (True):
    ret, img = cap.read() #"D:\Yolo Detection\MateImages\image311.jpg")
    if ret == False:
        break

    gray2 = converttoGrayImage(img)
    kpImg2, kpImg2Feat = siftFeature(gray2)

    # BF Matcher object which creates matching
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck= True)
    matches = bf.match(kptempImage1Feat, kpImg2Feat)

    # Sort matches in order of their distance
    matches = sorted(matches, key = lambda x:x.distance)

    #draw top N matches
    N_MATCHES = 50
    match_images = cv2.drawMatches(tempImage, kptempImage1, img, kpImg2, matches[:N_MATCHES], img.copy(), singlePointColor = (0,0,0) , flags = 0)

    cv2.imshow("matchImage", match_images)
    counter += 1
    k = cv2.waitKey(1)
    if k == ord("q"):
        cv2.destroyAllWindows()
        break
    if k == ord("n"):
        counter += 1
    if k == ord("b"):
        if counter > 0:
            counter -= 1
			
			
