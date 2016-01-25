import cv2 
import numpy as np 
width=640
height=400

# Create a black image
img = np.zeros((width,height,3), np.uint8) 

# Draw a green rectangle
cv2.rectangle(img,(10,10),(100,50),(0,255,0),3) 
fourcc = cv2.cv.CV_FOURCC(*'XVID')
video = cv2.VideoWriter('/tmp/test.avi',fourcc,20,(width,height)) 
for i in range(240):
	video.write(img)
video.release()

cap = cv2.VideoCapture("/tmp/test.avi") 
assert(cap.isOpened()) # True = read video successfully. False - fail to read 
cap.release()
cv2.destroyAllWindows()

