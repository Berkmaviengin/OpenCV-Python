import cv2
import numpy as np

gray_image = cv2.imread('image.png', 0)

fast = cv2.FastFeatureDetector()

keypoints = fast.detect(gray_image, None)
print "Number of keypoints with non max suppression:", len(keypoints)

img_keypoints_with_nonmax = cv2.drawKeypoints(gray_image, keypoints, color=(0,255,0))
cv2.imshow('FAST keypoints - with non max suppression', img_keypoints_with_nonmax)

fast.setBool('nonmaxSuppression', False)

keypoints = fast.detect(gray_image, None)

print "Total Keypoints without nonmaxSuppression:", len(keypoints)

img_keypoints_without_nonmax = cv2.drawKeypoints(gray_image, keypoints, color=(0,255,0))
cv2.imshow('FAST keypoints - without non max suppression', img_keypoints_without_nonmax)
cv2.waitKey()