import cv2
import numpy as np

img1 = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('butterfly.jpg', cv2.IMREAD_GRAYSCALE)
if img1 is None or img2 is None:
    raise Exception('영상 읽기 에러')

alpha, beta = 0.6, 0.7
add1 = cv2.add(img1, img2) # 두 영상을 단순히 합성 (saturate 연산)
add2 = cv2.add(img1 * alpha, img2 * beta) # 비율(ratio)을 곱해서 합성
add3 = np.clip(add2, 0, 255).astype('uint8')
   # 255보다 큰 값을 saturate 처리 (numpy clip 함수 이용)
add4 = cv2.addWeighted(img1, alpha, img2, beta, 0) # 비율(ratio)을 곱해서 합성

cv2.imshow('origin1', img1)
cv2.imshow('origin2', img2)
cv2.imshow('add1', add1)
cv2.imshow('add2', add2)
cv2.imshow('add3', add3)
cv2.imshow('add4', add4)
cv2.waitKey(0)