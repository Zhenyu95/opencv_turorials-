import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def sobel(img):
    grad_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    grad_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    grad_xy = cv.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

    plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(grad_x)
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(grad_y)
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(grad_xy)
    plt.title('Sobel XY'), plt.xticks([]), plt.yticks([])

    plt.show()

def scharr(img):
    grad_x = cv.Scharr(img, cv.CV_64F, 1, 0)
    grad_y = cv.Scharr(img, cv.CV_64F, 0, 1)
    grad_xy = cv.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

    plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(grad_x)
    plt.title('Scharr X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(grad_y)
    plt.title('Scharr Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(grad_xy)
    plt.title('Scharr XY'), plt.xticks([]), plt.yticks([])

    plt.show()

def laplacian(img):
    lapImg = cv.Laplacian(img,cv.CV_64F,ksize=1)
    plt.subplot(1, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1, 2, 2), plt.imshow(lapImg)
    plt.title(' Laplacian'), plt.xticks([]), plt.yticks([])

    plt.show()

img = cv.imread('Human.jpg')
#sobel(img)
#laplacian(img)
scharr(img)

cv.waitKey(0)
cv.destroyAllWindows()