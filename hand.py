import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def contours(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret1, thresh1 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    ret2, thresh2 = cv.threshold(gray, 110, 255, 0)

    thresh1 = cv.morphologyEx(thresh1,cv.MORPH_OPEN,cv.getStructuringElement(cv.MORPH_ELLIPSE,(40,40)))
    thresh2 = cv.morphologyEx(thresh2, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE, (40, 40)))

    thresh1 = cv.morphologyEx(thresh1,cv.MORPH_CLOSE,cv.getStructuringElement(cv.MORPH_ELLIPSE,(40,40)))
    thresh2 = cv.morphologyEx(thresh2, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (40, 40)))
    

    contours1, hierarchy1 = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy2 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    blank = np.zeros(img.shape, dtype=np.uint8)

    img1 = cv.drawContours(blank, contours1, 0, (0, 255, 0), 3)
    img2 = cv.drawContours(blank, contours2, 0, (0, 255, 0), 3)

    titles = ['Original', 'Ostu+Simple', 'Simple+Simple', 'AdaptiveMean+Simple', 'AdaptiveGaussian+Simple',
              'AdaptiveGaussian+None']
    imgs = [thresh1, img1, img2]
    # imgs = [img, thresh1, thresh2]

    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(imgs[i],'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


img = cv.imread('Hand.jpg')
contours(img)
cv.waitKey(0)
cv.destroyAllWindows()



