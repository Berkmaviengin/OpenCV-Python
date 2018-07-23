import cv2
import numpy as np
from matplotlib import pyplot as plt

res=cv2.imread('1.jpg',0)
a,th=cv2.threshold(res,180,255,cv2.THRESH_BINARY)
kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(th,kernel,iterations = 1)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
opening1 = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)

plt.subplot(221), plt.imshow(res, 'gray')
plt.subplot(222), plt.imshow(th,'gray')
plt.subplot(223), plt.imshow(opening1, 'gray')

plt.show()
