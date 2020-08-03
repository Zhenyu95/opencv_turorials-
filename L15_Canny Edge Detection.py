import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Scarlett.jpg')
def canny(img):
    edges = cv.Canny(img,50,150)

    plt.subplot(121),plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()
#canny(img)
