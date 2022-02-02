import cv2
import os 

video_path = "D:\\testVideoDrone\\DJI_0016.mp4"

img_path = "D:\\testVideoDrone\\testImages"

cap = cv2.VideoCapture(video_path)

#cap = cv2.VideoCapture("E:\Gazelle.mov")

counter  = 0
startLogging = True
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

while (True):
	# Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.namedWindow("Test", cv2.WINDOW_NORMAL)
    cv2.imshow("Test",frame)
    frame_no = cap.get(cv2.CAP_PROP_POS_FRAMES)
    print(f"Frame : {frame_no}")
	
    if startLogging:
        imagePath = os.path.join(img_path, str(frame_no) + ".jpg")
        cv2.imwrite( imagePath, frame )
    counter += 1
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
    if k == ord("s"):
        if startLogging:
            print ( "Logger Deactivated ")
            startLogging = False
        else:
            print("Logger Activated")
            startLogging = True
    if k == ord("j"): # Jumps 50 Frames
        nextFrame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        newFrame = nextFrame + 1000
        if newFrame < totalFrames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, newFrame)
        continue

cap.release()
cv2.destroyAllWindows()


