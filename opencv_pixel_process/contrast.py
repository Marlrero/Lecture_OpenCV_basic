import cv2
import numpy as np

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 오류')

empty = np.zeros(img.shape[:2], img.dtype) # 빈 영상(더미 영상)
avg = cv2.mean(img)[0] / 2.0 # 영상 화소 평균의 절반

r1 = cv2.scaleAdd(img, 0.5, empty) # 명암 대비 감소
r2 = cv2.scaleAdd(img, 2.0, empty) # 명암 대비 증가

# cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) -> dst
# saturate(src1*alpha + src2*beta + gamma)
r3 = cv2.addWeighted(img, 0.5, empty, 0, avg)
 # 명암 대비를 감소하고, 평균의 절반을 더해서 품질을 높임
r4 = cv2.addWeighted(img, 2.0, empty, 0, -avg)
 # 명암 대비를 증가하고, 평균의 절반을 빼서 품질을 높임

cv2.imshow('origin', img)
cv2.imshow('contrast decrease', r1)
cv2.imshow('contrast increase', r2)
cv2.imshow('contrast decrease(+avg)', r3)
cv2.imshow('contrast increase(-avg)', r4)
cv2.waitKey(0)