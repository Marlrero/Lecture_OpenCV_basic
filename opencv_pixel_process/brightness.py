import cv2
import numpy as np

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Origin', img)

# OpenCV 함수 이용 (saturation)
r1 = cv2.add(img, 100)  # 영상 밝게
r2 = cv2.subtract(img, 100) # 영상 어둡게

# Numpy의 ndarray 이용 (modulo)
r3 = img + 100
r4 = img - 100

cv2.imshow('Origin', img)
cv2.imshow('bright-OpenCV', r1)
cv2.imshow('dark-OpenCV', r2)
cv2.imshow('bright-Numpy', r3)
cv2.imshow('dark-Numpy', r4)
cv2.waitKey(0)