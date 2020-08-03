import cv2 as cv
import numpy as np

def biLateralEPF(img):
    dst = cv.bilateralFilter(img,0,100,15)
    cv.imshow('biEPF',dst)

def meanShiftEPF(img):
    dst = cv.pyrMeanShiftFiltering(img,10,50)
    cv.imshow('meanEPF',dst)

img = cv.imread('Human.jpg')
cv.imshow('Original',img)
biLateralEPF(img)
meanShiftEPF(img)


cv.waitKey(0)
cv.destroyAllWindows()