import cv2 as cv
import numpy as np

def hough(img):
    # must convert to gray scale first
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # use Canny to get the edges
    edges = cv.Canny(gray, 60, 120, apertureSize=3)
    # cv.imwrite('binary.jpg', edges)
    # get the lines, the forth parameter sets the min "votes" for a line
    lines = cv.HoughLines(edges, 1, np.pi / 180, 350, None, 0, 0)
    # draw the lines on the image and write the image
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imwrite('result.jpg', img)

img = cv.imread('Subpack.jpg')
hough(img)

cv.waitKey(0)
cv.destroyAllWindows()
