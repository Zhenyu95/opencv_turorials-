import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def simThresh(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.THRESH_BINARY: thresholded img = 255 if dst(x,y)>127 else 0
    ret, thresh1 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    # cv.THRESH_BINARY_INV: thresholded img = 255 if dst(x,y)>127 else 0
    ret, thresh2 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
    # cv.THRESH_TRUNC: thresholded img = threshold (127 in this case) if dst(x,y)>127 else src(x,y)
    ret, thresh3 = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)
    # cv.THRESH_TOZERO: thresholded img = src(x,y) if dst(x,y)>127 else 0
    ret, thresh4 = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
    # cv.THRESH_TOZERO: thresholded img = 0 if dst(x,y)>127 else src(x,y)
    ret, thresh5 = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO_INV)
    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [gray, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def otsuThresh(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    print(ret)
    titles = ['Original Img', 'Otsu']
    images = [gray, thresh]
    for i in range(2):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def triangleThresh(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY+cv.THRESH_TRIANGLE)
    print(ret)
    titles = ['Original Img', 'Otsu']
    images = [gray, thresh]
    for i in range(2):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def adptiveThres(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, th1 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    # cv.adaptiveThreshold(	src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])
    th2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    th3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
              'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [gray, th1, th2, th3]
    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


img = cv.imread('Human.jpg')
#simThresh(img)
#triangleThresh(img)
adptiveThres(img)

cv.waitKey(0)
cv.destroyAllWindows()