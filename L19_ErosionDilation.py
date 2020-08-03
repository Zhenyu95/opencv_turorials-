import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def erosion(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    kernel3 = np.ones((3, 3),np.uint8)
    erosion3 = cv.erode(thresh, kernel3)

    kernel5 = np.ones((5, 5), np.uint8)
    erosion5 = cv.erode(thresh, kernel5)

    kernel7 = np.ones((27, 27), np.uint8)
    erosion7 = cv.erode(thresh, kernel7)


    titles = ['original', 'erosion 3*3', 'erosion 5*5', 'erosion 7*7', 'dilation 3*3', 'dilation 5*5', 'dilation 7*7']
    imgs = [thresh, erosion3, erosion5, erosion7]

    for i in range(4):
        plt.subplot(1, 4, i + 1)
        plt.imshow(imgs[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def dilation(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    kernel3 = np.ones((3, 3), np.uint8)
    dilation3 = cv.dilate(thresh, kernel3)

    kernel5 = np.ones((5, 5), np.uint8)
    dilation5 = cv.dilate(thresh, kernel5)

    kernel7 = np.ones((27, 27), np.uint8)
    dilation7 = cv.dilate(thresh, kernel7)

    titles = ['original', 'dilation 3*3', 'dilation 5*5', 'dilation 7*7']
    imgs = [thresh, dilation3, dilation5, dilation7]

    for i in range(4):
        plt.subplot(1, 4, i + 1)
        plt.imshow(imgs[i],'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def opening(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    kernel3 = np.ones((3, 3), np.uint8)
    opening3 = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel3)

    kernel5 = np.ones((5, 5), np.uint8)
    opening5 = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel5)

    kernel7 = np.ones((27, 27), np.uint8)
    opening7 = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel7)

    titles = ['original', 'dilation 3*3', 'dilation 5*5', 'dilation 7*7']
    imgs = [thresh, opening3, opening5, opening7]

    for i in range(4):
        plt.subplot(1, 4, i + 1)
        plt.imshow(imgs[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
        plt.show()

def closing(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    kernel3 = np.ones((3, 3), np.uint8)
    closing3 = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel3)

    kernel5 = np.ones((5, 5), np.uint8)
    closing5 = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel5)

    kernel7 = np.ones((27, 27), np.uint8)
    closing7 = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel7)

    titles = ['original', 'dilation 3*3', 'dilation 5*5', 'dilation 7*7']
    imgs = [thresh, closing3, closing5, closing7]

    for i in range(4):
        plt.subplot(1, 4, i + 1)
        plt.imshow(imgs[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

img = cv.imread('Scarlett.jpg')
# erosion(img)
# dilation(img)
# opening(img)
closing(img)
cv.waitKey(0)
cv.destroyAllWindows()