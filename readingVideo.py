import numpy as np
import cv2

cap = cv2.VideoCapture(0)
from skimage.exposure.exposure import rescale_intensity
#cap = cv2.VideoCapture("D:\\Termites\\N04HHS2017-V4.mp4")
#cap = cv2.VideoCapture("D:\Yolo Detection\Video\FinchVideo.mp4")

def showVideo( name, data):
    "Function to show the image"
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 640, 480)
    cv2.imshow(name, data)
    return;


counter = 1

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (480,640), cv2.INTER_CUBIC)

    #threshold the image
    ret,binImage = cv2.threshold(gray, 130 ,255,cv2.THRESH_BINARY)
    

   # Display the resulting frame
    showVideo('frame',gray)
    showVideo('bin', binImage)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
