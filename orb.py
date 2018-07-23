import cv2
import numpy as np

input_image = cv2.imread('image.png')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 

orb = cv2.ORB()

keypoints = orb.detect(gray_image, None)

keypoints, descriptors = orb.compute(gray_image, keypoints)

final_keypoints = cv2.drawKeypoints(input_image, keypoints, color=(0,255,0), flags=0)

cv2.imshow('ORB keypoints', final_keypoints)
cv2.waitKey()
