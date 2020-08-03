import cv2 as cv
import numpy as np

def img_add(img1,img2):
    dst = cv.add(img1,img2)
    cv.imshow('added',dst)

def img_subtract(img1,img2):
    dst = cv.subtract(img1,img2)
    cv.imshow('subtracted',dst)

def img_devide(img1,img2):
    dst = cv.divide(img1,img2)
    cv.imshow('devided',dst)

def img_multiply(img1,img2):
    dst = cv.multiply(img1,img2)
    cv.imshow('multiplied',dst)

def img_and(img1,img2):
    dst = cv.bitwise_and(img1,img2)
    cv.imshow('and',dst)

def img_or(img1,img2):
    dst = cv.bitwise_or(img1,img2)
    cv.imshow('or',dst)

def contrast_brightness(img, contrast, brightness):
    blank = np.zeros(img.shape,img.dtype)
    dst = cv.addWeighted(img, contrast, blank, 1-contrast, brightness)
    cv.imshow('contrast_brightness',dst)

img1 = cv.imread('Experiment.png')
img2 = cv.imread('x-ray.png')

cv.imshow('Exp',img1)
cv.imshow('x-ray',img2)

# img_add(img1,img2)
# img_subtract(img1,img2)
# img_devide(img1,img2)
# img_multiply(img1,img2)

# img_and(img1,img2)
# img_or(img1,img2)

contrast_brightness(img1,2,1)

cv.waitKey(0)