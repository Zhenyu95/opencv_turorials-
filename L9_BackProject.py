import cv2 as cv
import numpy as np

target = cv.imread('Explosion.jpg')
sample = cv.imread('Explosion_partial.jpg')

def backProjct(target,sample):
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[36,48],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    cv.imshow('backProject',dst)

cv.imshow('sample',sample)
cv.imshow('target',target)
backProjct(target,sample)

cv.waitKey(0)
cv.destroyAllWindows()
