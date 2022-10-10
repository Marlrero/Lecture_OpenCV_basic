import cv2
from differential import get_differential

img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

mask1 = [
    -1, 0, 0,
     0, 1, 0,
     0, 0, 0
]
mask2 = [
    0, 0, -1,
    0, 1,  0,
    0, 0,  0
]

dst, dst1, dst2 = get_differential(img, mask1, mask2)

cv2.imshow('origin', img)
cv2.imshow('roberts edge', dst) # 최종 로버츠 마스크 적용한 에지 검출
cv2.imshow('dst1', dst1) # 대각선 방향 첫번째 마스크 에지 검출
cv2.imshow('dst2', dst2) # 대각선 방향 두번째 마스크 에지 검출
cv2.waitKey(0)