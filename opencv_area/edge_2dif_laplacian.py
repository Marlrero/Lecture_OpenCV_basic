import cv2
import numpy as np

img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

four_direcion_mask = [
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
]
eight_direction_mask = [
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
]

four_direcion_mask = np.array(four_direcion_mask, np.int16) # 음수로 인해 int16
eight_direction_mask = np.array(eight_direction_mask, np.int16)

dst1 = cv2.filter2D(img, cv2.CV_16S, four_direcion_mask) # CV_16S (16bit signed int)
dst2 = cv2.filter2D(img, cv2.CV_16S, eight_direction_mask)
dst3 = cv2.Laplacian(img, cv2.CV_16S, 1) # ksize = 1이면 3x3 라플라시안 필터

cv2.imshow('origin', img)
cv2.imshow('filter2D 4', cv2.convertScaleAbs(dst1)) # 절댓값 + CV_8U 변환
cv2.imshow('filter2D 8', cv2.convertScaleAbs(dst2))
cv2.imshow('OpenCV Laplacian', cv2.convertScaleAbs(dst3))
cv2.waitKey(0)