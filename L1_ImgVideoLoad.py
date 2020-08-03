import cv2 as cv

def get_img_info(img):
    print(type(img))
    print(img.shape)
    print(img.size)
    print(img.dtype)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for ch in range(img.shape[2]):
                pv = img[row,col,ch]
                img[row,col,ch] = 255 - pv
    cv.imshow("demo",img)

def video_load():
    capture = cv.VideoCapture(1)
    while True:
        ret, frame = capture.read()
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            break

def inverse(img):
    img = cv.bitwise_not(img)
    cv.imshow("inverse_demo",img)

src = cv.imread('Explosion.jpg')
cv.namedWindow("input Img",cv.WINDOW_AUTOSIZE)
cv.imshow("input Img",src)
t1 = cv.getTickCount()
inverse(src)
t2 = cv.getTickCount()
rtime = (t2-t1)/cv.getTickFrequency()
print(rtime)
#video_load()
cv.waitKey(0)

cv.destroyAllWindows()