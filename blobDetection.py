import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
from skimage.exposure.exposure import rescale_intensity

#cap = cv2.VideoCapture("D:\\Termites\\N04HHS2017-V4.mp4")
cap = cv2.VideoCapture("D:\\testVideos\\VID_20190516_192528094.mp4")

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

    if counter == 1:
        print("Before compression", gray.shape) # height(rows), width(cols)
        print("After compression", resized.shape)
        counter = counter + 1

    #threshold the image
    ret,binImage = cv2.threshold(gray, 130 ,255,cv2.THRESH_BINARY)

    #blob detector
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 100;
    params.maxThreshold = 200;

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 80
    params.maxArea = 250

    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.1

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.8

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.1
    params.maxInertiaRatio = 0.5

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(resized)
    im_with_keypoints = cv2.drawKeypoints(resized, keypoints, np.array([]), (0, 0, 255),
                                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    datapoints = keypoints
    for keypoint in keypoints:
        x = keypoint.pt[0]
        y = keypoint.pt[1]
        s = keypoint.size
        print('Keypoints' ,x,y,s)

   # Display the resulting frame
   # showVideo('frame',gray)
    showVideo('Blobber', im_with_keypoints)
    showVideo('bin', binImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
