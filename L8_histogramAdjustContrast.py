import cv2 as cv
import numpy as np

def equalHist(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('Gray',gray)
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist',dst)

def clache(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    clache = cv.createCLAHE(clipLimit=2, tileGridSize=(8,8))
    dst = clache.apply(gray)
    cv.imshow('Clache',dst)

def histCompare(img1,img2):
    hist1 = cv.calcHist([img1],[0,1,2],None,[16,16,16],[0,256, 0,256, 0,256])
    hist2 = cv.calcHist([img2],[0,1,2],None,[16,16,16],[0,256, 0,256, 0,256])
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("Bhatta:%s, Correlation:%s, ChiSQR:%s" %(match1, match2, match3))

def hsv_compare(img1,img2):
    hsv_img1 = cv.cvtColor(img1,cv.COLOR_BGR2HSV)
    hsv_img2 = cv.cvtColor(img2,cv.COLOR_BGR2HSV)

    h_bins = 50
    s_bins = 60
    histSize = [h_bins,s_bins]

    h_ranges = [0,180]
    v_ranges = [0,256]
    ranges = h_ranges + v_ranges

    channels = [0,1]

    hist1 = cv.calcHist([img1],channels,None,histSize,ranges,accumulate=False)
    cv.normalize(hist1,hist1,alpha=0,beta=255,norm_type=cv.NORM_MINMAX)
    hist2 = cv.calcHist([img2],channels,None,histSize,ranges,accumulate=False)
    cv.normalize(hist2,hist2,alpha=0,beta=255,norm_type=cv.NORM_MINMAX)

    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("Bhatta:%s, Correlation:%s, ChiSQR:%s" %(match1, match2, match3))

   
    

img1 = cv.imread('Explosion.jpg')
img2 = cv.imread('Explosion2.jpg')

hsv_compare(img1,img2)

# histCompare(img1,img2)

# equalHist(img)
# clache(img)


cv.waitKey(0)
cv.destroyAllWindows()