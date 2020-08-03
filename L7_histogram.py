import cv2 as cv
import numpy as np
from matplotlib import pyplot

def plot(img):
    pyplot.hist(img.ravel(),255,[0,256])
    pyplot.show()

def img_hist(img):
    color = ('blue','green','red')
    for i, color in enumerate(color):
        hist = cv.calcHist([img],[i],None,[256],[0,256])
        pyplot.plot(hist,color=color)
        pyplot.xlim([0,256])
    pyplot.show()

img = cv.imread('Explosion.jpg')
cv.imshow('Original',img)
#plot(img)
img_hist(img)



cv.waitKey(0)
cv.destroyAllWindows()