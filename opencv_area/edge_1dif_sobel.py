import cv2
import numpy as np
from differential import get_differential

img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

vertical_mask = [
    -1, 0, 1,
    -2, 0, 2,
    -1, 0, 1
]
horizontal_mask = [
    -1, -2, -1,
     0,  0,  0,
     1,  2,  1
]

dst, dst1, dst2 = get_differential(img, vertical_mask, horizontal_mask)

#dst_o1 = cv2.Sobel(np.float32(img), cv2.CV_32F, 1, 0, 3) # x방향 미분 3x3 커널
#dst_o1 = cv2.convertScaleAbs(dst_o1) # 절댓값, unit8(CV_8U)로 형변환
#dst_o2 = cv2.Sobel(np.float32(img), cv2.CV_32F, 0, 1, 3) # y방향 미분 3x3 커널
#dst_o2 = cv2.convertScaleAbs(dst_o1) # 절댓값, unit8(CV_8U)로 형변환

cv2.imshow('origin', img)
cv2.imshow('sobel edge', dst) # 최종 소벨 마스크 적용한 에지 검출
cv2.imshow('vertical mask', dst1) # 수직 방향 마스크 에지 검출
cv2.imshow('horizontal mask', dst2) # 수평 방향 마스크 에지 검출
#cv2.imshow('OpenCV sobel edge', dst_o1)
cv2.waitKey(0)