import cv2
import numpy as np

gray_image = cv2.imread('image.png', 0)

star = cv2.FeatureDetector_create("STAR")

brief = cv2.DescriptorExtractor_create("BRIEF")

keypoints = star.detect(gray_image, None)

keypoints, descriptors = brief.compute(gray_image, keypoints)

gray_keypoints = cv2.drawKeypoints(gray_image, keypoints, color=(0,255,0))
cv2.imshow('BRIEF keypoints', gray_keypoints)
cv2.waitKey()
