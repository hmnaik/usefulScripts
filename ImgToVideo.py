import cv2
import glob
import time


outputVideo = cv2.VideoWriter('testBird.mp4',0x00000020, 30.0, (1280,720), True)
windowName = 'imageSec'
cv2.namedWindow(windowName,cv2.WINDOW_NORMAL)

#imageList = glob.glob("D:\\Yolo Detection\\finchImages\\TestResults\\*.jpg")

for img in glob.glob("D:\\Yolo Detection\\finchImages\\TestResults\\*.jpg"):
    frame = cv2.imread(img)
    if frame is not None:
        cv2.imshow(windowName, frame)
        cv2.waitKey(1) # Required for reading the image
        outputVideo.write(frame)

# Release the video commands
outputVideo.release()
cv2.destroyAllWindows()