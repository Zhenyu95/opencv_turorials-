import cv2 as cv
import numpy as np

img = cv.imread("Explosion.jpg")
cv.imshow('original',img)

b, g, r = cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
#delete specific channel: red
img[:,:, 2] = 0
cv.imshow('without red',img)
#merge the channels
img = cv.merge([b, g, r])
cv.imshow('new',img)

cv.waitKey(0)