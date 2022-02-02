
import cv2 as cv
import numpy as np

bgimgSet = False
cap = cv.VideoCapture(1)
#Default first img as background image
ret,bgimg = cap.read()
subimg = bgimg.copy()
while(True):

    ret,img = cap.read()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Error message for ret
    key = cv.waitKey(10)
    if key == ord('b'):
        bgimgSet = True
        bgimg = img.copy()
        cv.namedWindow("BgImg", cv.WINDOW_NORMAL)
        cv.imshow("BgImg", bgimg)
    if key == ord('c'):
        break
    if key == ord('s'):
        if (bgimgSet):
            subimg =  cv.subtract(bgimg, img)

    cv.namedWindow("SubImg", cv.WINDOW_NORMAL)
    cv.imshow("SubImg", subimg)

    cv.namedWindow("img", cv.WINDOW_NORMAL)
    cv.imshow("img", img)

cap.release()
cv.destroyAllWindows()


