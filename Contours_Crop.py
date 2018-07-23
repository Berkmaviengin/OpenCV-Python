import numpy as np
import cv2
import math

image= cv2.imread('pll.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resim = cv2.resize(gray_image, None, fx=1.4, fy=1.4, interpolation=cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(resim, (5, 5), 0)

ret,thresh=cv2.threshold(blur,120,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Thresh0',thresh)

im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

x,y,w,h = cv2.boundingRect(cnt)
imcrop=resim[y:y+h,x:x+w]

cv2.imshow('crop',imcrop)

cv2.waitKey(0)
cv2.destroyAllWindows()