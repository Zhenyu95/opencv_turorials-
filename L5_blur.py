import cv2 as cv
import numpy as np

def img_blur(img):
    dst = cv.blur(img,(10,10))
    cv.imshow('blurred',dst)

def customized_kernel(img):
    kernel = np.ones([3,3],np.float32)*(-1)
    kernel[1,1] = 9
    dst = cv.filter2D(cv.blur(img,(10,10)),-1,kernel)
    cv.imshow('sharped',dst)

img = cv.imread('Explosion.jpg')
cv.imshow('original',img)
img_blur(img)
customized_kernel(img)

cv.waitKey(0)
cv.destroyAllWindows()