import cv2
import numpy as np

from filter import mat_filter
# 행렬 적용 방식이 그대로 사용됨. 단지 마스크만 바뀔 뿐임.

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

kernel1 = [
     0, -1, 0,
    -1,  5,-1,
     0, -1, 0
] # 1D 리스트
kernel2 = [
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
] # 2D 리스트

kernel1 = np.array(kernel1, np.float32).reshape(3, 3) # 1D -> 3x3 2D
kernel2 = np.array(kernel2, np.float32) # 2D

sharp1 = cv2.convertScaleAbs(mat_filter(img, kernel1))
sharp2 = cv2.convertScaleAbs(mat_filter(img, kernel2))

cv2.imshow('origin', img)
cv2.imshow('sharp1', sharp1)
cv2.imshow('sharp2', sharp2)
cv2.waitKey(0)