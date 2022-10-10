import cv2
import numpy as np

img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

gaussian = cv2.GaussianBlur(img, (7, 7), 0, 0)
# 7x7 마스크에 표준편차 값을 모두 0으로 지정하면 마스크 크기에 맞게 표준편차 계산됨
log = cv2.Laplacian(gaussian, cv2.CV_16S, 7) # 7x7 마스크, 음수값 포함위해 16bit integer

# 표준편차가 다른 2개의 가우시안 필터링 수행
gaussian1 = cv2.GaussianBlur(img, (3, 3), 0, 0)
gaussian2 = cv2.GaussianBlur(img, (9, 9), 0, 0)
dog = gaussian1 - gaussian2

cv2.imshow('origin', img)
cv2.imshow('LoG', log.astype('uint8')) # 형 변환 후 영상 표시
cv2.imshow('DoG', dog)
cv2.waitKey(0)