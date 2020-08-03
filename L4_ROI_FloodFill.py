import cv2 as cv
import numpy as np

def floodfill(img):
    h, w = img.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(img,mask,(1,1),(255,0,0),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('floodfill',img)

img = cv.imread('Explosion.jpg')
cv.imshow('original',img)
# part = img[100:500,100:500]
# part = cv.cvtColor(part,cv.COLOR_BGR2GRAY)
# part = cv.cvtColor(part,cv.COLOR_GRAY2BGR)
# img[100:500,100:500] = part
# cv.imshow('ROI',img)
floodfill(img)

cv.waitKey(0)
cv.destroyAllWindows()
