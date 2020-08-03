import cv2 as cv
import numpy as np

def tempMatch(src,temp):
    methods = [
        #the actual value of them are int, ranging from 0 to 5
        cv.TM_SQDIFF,
        cv.TM_SQDIFF_NORMED,
        cv.TM_CCORR,
        cv.TM_CCORR_NORMED,
        cv.TM_CCOEFF,
        cv.TM_CCOEFF_NORMED
    ]
    tempH, tempW = temp.shape[:2]
    for method in methods:
        match = cv.matchTemplate(src,temp,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(match)
        #For the first two methods ( CV_SQDIFF and CV_SQDIFF_NORMED ) the best match are the lowest values. 
        #For all the others, higher values represent better matches.
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            topleft = min_loc
        else:
            topleft = max_loc
        #draw a rectangle to highlight template matching result
        botright = (topleft[0]+tempW,topleft[1]+tempH)
        cv.rectangle(src,topleft,botright,(0,0,255),2)
        cv.imshow('method'+str(method),src)


src = cv.imread('Explosion.jpg')
temp = cv.imread('Explosion_partial.jpg')

cv.imshow('source',src)
cv.imshow('temp',temp)
tempMatch(src,temp)

cv.waitKey(0)
cv.destroyAllWindows()
