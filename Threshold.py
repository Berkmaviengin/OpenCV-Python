import cv2
import numpy as np

a=cv2.imread('image.png',0) #read image
ret,th=cv2.threshold(a,160,255,cv2.THRESH_BINARY) #thresh binary image
cv2.imshow('th',th) #show binary image

cv2.waitKey(0)
cv2.destroyAllWindows()
