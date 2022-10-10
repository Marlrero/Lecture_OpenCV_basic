# edge_1dif_prewitt.py
import cv2
from differential import get_differential

img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

vertical_mask = [
    -1, 0, 1,
    -1, 0, 1,
    -1, 0, 1
]
horizontal_mask = [
    -1, -1, -1,
     0,  0,  0,
     1,  1,  1
]

dst, dst1, dst2 = get_differential(img, vertical_mask, horizontal_mask)

cv2.imshow('origin', img)
cv2.imshow('prewitt edge', dst) # 최종 프리윗 마스크 적용한 에지 검출
cv2.imshow('vertical mask', dst1) # 수직 방향 마스크 에지 검출
cv2.imshow('horizontal mask', dst2) # 수평 방향 마스크 에지 검출
cv2.waitKey(0)
