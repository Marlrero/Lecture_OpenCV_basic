import cv2
import numpy as np

img = cv2.imread('pyramid.jpg', cv2.IMREAD_COLOR)
if img is None:
    raise Exception('영상파일 열기 실패')

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
#a = np.arange(1, 7).reshape(2, 3)
b = a.T # transpose
print(a)
print(b)

t = cv2.transpose(img)
cv2.imshow('origin', img)
cv2.imshow('transpose', t)
cv2.waitKey(0)