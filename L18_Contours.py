import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def contours(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret1, thresh1 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    ret2, thresh2 = cv.threshold(gray, 127, 255, 0)
    thresh3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    thresh4 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

    contours1, hierarchy1 = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy2 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours3, hierarchy3 = cv.findContours(thresh3, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours4, hierarchy4 = cv.findContours(thresh4, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours5, hierarchy5 = cv.findContours(thresh4, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    img = np.zeros(img.shape, dtype=np.uint8)

    img1 = cv.drawContours(img, contours1, -1, (0, 255, 0), 3)
    img2 = cv.drawContours(img, contours2, -1, (0, 255, 0), 3)
    img3 = cv.drawContours(img, contours3, -1, (0, 255, 0), 3)
    img4 = cv.drawContours(img, contours4, -1, (0, 255, 0), 3)
    img5 = cv.drawContours(img, contours5, -1, (0, 255, 0), 3)

    titles = ['Original', 'Ostu+Simple', 'Simple+Simple', 'AdaptiveMean+Simple', 'AdaptiveGaussian+Simple',
              'AdaptiveGaussian+None']
    imgs = [img,img1,img2,img3,img4,img5]
    imgs = [img,thresh1,thresh2,thresh3,thresh4,thresh4]

    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(imgs[i])
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

img = cv.imread('Hand.jpg')
contours(img)
cv.waitKey(0)
cv.destroyAllWindows()



