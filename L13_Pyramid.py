import cv2 as cv
import numpy as np

def gaussainPyramid(img):
    temp = img.copy()
    gaussianPyrImg = [img]
    for i in range(6):
        temp = cv.pyrDown(temp)
        #cv.imshow('Gaussian'+str(i), temp)
        gaussianPyrImg.append(temp)
    return gaussianPyrImg

def laplacianPyramid(img):
    gaussianPyrImg = gaussainPyramid(img)
    laplacianPyrImg = [gaussianPyrImg[5]]
    for i in range(5, 0, -1):
        GE = cv.pyrUp(gaussianPyrImg[i])
        L = cv.subtract(gaussianPyrImg[i - 1], GE)
        #cv.imshow('Laplacian'+str(i),L)
        laplacianPyrImg.append(L)
    #return laplacianPyrImg

img = cv.imread('8Kleaves.jpg')
laplacianPyramid(img)

cv.waitKey(0)
cv.destroyAllWindows()