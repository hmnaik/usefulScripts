import numpy as np
import cv2


#cap = cv2.VideoCapture('D:\\Termites\\test.mp4')
fileName = "testVideos\\VID_20190516_192528094" # "Termites\\test"
cap = cv2.VideoCapture('D:\\'+fileName+'.mp4')
#cap = cv2.VideoCapture("D:\Yolo Detection\Video\MateFeeding.avi")

codec = cv2.VideoWriter_fourcc('D','I','V','X')
out = cv2.VideoWriter('D:\\'+fileName+'output.avi', codec, 30.0, (1080,720) )#(4096, 2160) )
# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 20,
                       qualityLevel = 0.6,
                       minDistance = 20,
                       blockSize = 5 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (7,7),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY) # Convert to gray scale
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
iterator = 0;
while(1):
    iterator += 1
    if iterator == 5:
        # ret, old_frame = cap.read()
        # old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)  # Convert to gray scale
        # p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
        mask = np.zeros_like(old_frame)
        iterator = 0

    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame',img)

    # Writing the image to video file
    dst = cv2.resize(img,(1080,720),interpolation= cv2.INTER_CUBIC)
    out.write(dst)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)


cap.release()
out.release()
cv2.destroyAllWindows()