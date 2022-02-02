import cv2
import numpy as np

# Testing to read images and display
image = cv2.imread('..\data\empire.jpg',0)

rows,cols = image.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(image, M ,(cols,rows))

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image',image)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
