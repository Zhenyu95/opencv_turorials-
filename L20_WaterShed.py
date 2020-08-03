import cv2 as cv
import numpy as np

def waterShed(img):
    # EPF Noise removal
    img = cv.pyrMeanShiftFiltering(img, 5, 20)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    cv.imshow('binary',thresh)

    # noise removal
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=4)
    cv.imshow('closing', closing)

    # sure background area
    sure_bg = cv.dilate(thresh, kernel, iterations=3)
    cv.imshow('sure bg',sure_bg)
    # find sure background area
    distance_transform = cv.distanceTransform(thresh, cv.DIST_L2, 5)
    cv.imshow('distance transform',distance_transform)
    ret, sure_fg = cv.threshold(distance_transform, 0.9*distance_transform.max(), 255, 0)
    cv.imshow('sure fg',sure_fg)

    # find unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)
    cv.imshow('unknown',unknown)

    # Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]
    
    cv.imshow('result',img)
img = cv.imread('coin.jpg')

waterShed(img)

cv.waitKey(0)
cv.destroyAllWindows()