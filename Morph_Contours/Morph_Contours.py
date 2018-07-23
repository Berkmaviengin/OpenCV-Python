def showfig(image, ucmap):
    if len(image.shape)==3 :
        b,g,r = cv2.split(image)       # get b,g,r
        image = cv2.merge([r,g,b])     # switch it to rgb
    imgplot=plt.imshow(image, ucmap)
    imgplot.axes.get_xaxis().set_visible(False)
    imgplot.axes.get_yaxis().set_visible(False)

#import Opencv library
try:
    import cv2
except ImportError:
    print ("You must have OpenCV installed")
import matplotlib.pyplot as plt
import numpy as np

Goster=True

plt.rcParams['figure.figsize'] = 10, 10

# Actual Code starts here
plt.title('Sample Car')
image_path="1.jpg"
carsample=cv2.imread(image_path)
showfig(carsample,None)
plt.rcParams['figure.figsize'] = 7,7

# convert into grayscale
gray_carsample=cv2.cvtColor(carsample, cv2.COLOR_BGR2GRAY)

if Goster is True:
    cv2.imshow('Gri', gray_carsample)

blur=cv2.GaussianBlur(gray_carsample,(5,5),0)

if Goster is True:
    cv2.imshow('Blur', blur)

sobelx=cv2.Sobel(blur, cv2.CV_8U, 2, 0, ksize=3)
if Goster is True:
    cv2.imshow('Sobel',sobelx)
ret,th2=cv2.threshold(sobelx, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
if Goster is True:
    cv2.imshow('Thresh',th2)
se=cv2.getStructuringElement(cv2.MORPH_RECT,(23,2))
closing=cv2.morphologyEx(th2, cv2.MORPH_CLOSE, se)
if Goster is True:
    cv2.imshow('Morp+Closing',closing)
rescnt,contours,hierarcy=cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    rect=cv2.minAreaRect(cnt)
    box=cv2.boxPoints(rect)
    box=np.int0(box)
    cv2.drawContours(carsample, [box], 0, (0,255,0),2)
cv2.imshow('aa',carsample)
showfig(carsample, None)
def validate(cnt):
    rect=cv2.minAreaRect(cnt)
    box=cv2.boxPoints(rect)
    box=np.int0(box)
    output=False
    width=rect[1][0]
    height=rect[1][1]
    if ((width!=0) & (height!=0)):
        if (((height/width>2) & (height>width)) | ((width/height>1) & (width>height))):
            if((height*width<16000) & (height*width>3000)):
                output=True
    return output

#Lets draw validated contours with red.
for cnt in contours:
    if validate(cnt):
        rect=cv2.minAreaRect(cnt)
        box=cv2.boxPoints(rect)
        box=np.int0(box)
        cv2.drawContours(carsample, [box], 0, (0,0,255),2)
cv2.imshow('b',carsample)

cv2.waitKey(0)
cv2.destroyAllWindows()