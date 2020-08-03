import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def houghCircle(img):
    img1 = cv.medianBlur(cv.cvtColor(img,cv.COLOR_BGR2GRAY),5)
    img2 = cv.cvtColor(cv.pyrMeanShiftFiltering(img, 10, 100),cv.COLOR_BGR2GRAY)
    img3 = cv.GaussianBlur(cv.cvtColor(img,cv.COLOR_BGR2GRAY),(7,7),2,2)

    cimg1 = cv.cvtColor(img1,cv.COLOR_GRAY2BGR)
    cimg2 = cv.cvtColor(img2, cv.COLOR_GRAY2BGR)
    cimg3 = cv.cvtColor(img3, cv.COLOR_GRAY2BGR)

    circles1 = cv.HoughCircles(img1, cv.HOUGH_GRADIENT, 1, 50, param1=200, param2=80, minRadius=20, maxRadius=0)
    circles2 = cv.HoughCircles(img2, cv.HOUGH_GRADIENT, 1, 50, param1=200, param2=80, minRadius=20, maxRadius=0)
    circles3 = cv.HoughCircles(img3, cv.HOUGH_GRADIENT, 1, 50, param1=200, param2=90, minRadius=20, maxRadius=0)

    circles1 = np.uint16(np.around(circles1))
    circles2 = np.uint16(np.around(circles2))
    circles3 = np.uint16(np.around(circles3))

    for i in circles1[0,:]:
        # draw the outer circle
        cv.circle(cimg1,(i[0],i[1]),i[2],(0,0,255),5)
        # draw the center of the circle
        cv.circle(cimg1,(i[0],i[1]),2,(0,0,255),5)
    for i in circles2[0,:]:
        # draw the outer circle
        cv.circle(cimg2,(i[0],i[1]),i[2],(0,0,255),5)
        # draw the center of the circle
        cv.circle(cimg2,(i[0],i[1]),2,(0,0,255),5)
    for i in circles3[0,:]:
        # draw the outer circle
        cv.circle(cimg3,(i[0],i[1]),i[2],(0,0,255),5)
        # draw the center of the circle
        cv.circle(cimg3,(i[0],i[1]),2,(0,0,255),5)

    plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(cimg1)
    plt.title('Median'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(cimg2)
    plt.title('Mean'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(cimg3)
    plt.title('Gaussian'), plt.xticks([]), plt.yticks([])
    plt.show()


img = cv.imread('Circle.jpg')
houghCircle(img)

cv.waitKey(0)
cv.destroyAllWindows()

