import cv2
import numpy as np

from morphology import erode, dilate # 직접 만든 함수 import

def opening(img, mask):
    return dilate(erode(img, mask), mask) # 침식 후 팽창

def closing(img, mask):
    return erode(dilate(img, mask), mask) # 팽창 후 침식

img = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상 읽기 에러")

mask = [0, 1, 0,   # 침식/팽창 마스크
        1, 1, 1,
        0, 1, 0]
mask = np.array(mask, np.uint8).reshape(3, 3)
bi_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
 # 영상 이진화(128보다 작으면 0, 128 이상이면 255 지정)

direct1 = opening(bi_img, mask)
direct2 = closing(bi_img, mask)
opencv1 = cv2.morphologyEx(bi_img, cv2.MORPH_OPEN, mask)
opencv2 = cv2.morphologyEx(bi_img, cv2.MORPH_CLOSE, mask, iterations=1)

cv2.imshow("image", img)
cv2.imshow("binary image", bi_img)
cv2.imshow("User open", direct1)
cv2.imshow("User close", direct2)
cv2.imshow("OpenCV open", opencv1)
cv2.imshow("OpenCV close", opencv2)
cv2.waitKey(0)