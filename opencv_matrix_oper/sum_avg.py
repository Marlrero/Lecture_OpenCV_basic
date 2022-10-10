import cv2
import numpy as np

img = cv2.imread("pyramid.jpg", cv2.IMREAD_COLOR)
if img is None: raise Exception("영상 읽기 에러")

mask = np.zeros(img.shape[:2], np.uint8) # 이미지의 가로, 세로 크기만큼 0으로 채운 행렬
mask[50:100, 50:100] = 255 # (50, 50) ~ (100, 100)까지의 원소를 255(흰색)으로 변경

sum_val = cv2.sumElems(img)  # 채널별 픽셀값 합
mean_val1 = cv2.mean(img)    # 채널별 픽셀값 평균
mean_val2 = cv2.mean(img, mask)  # 특정 마스크 영역만 픽셀값 평균

print(f'sum_val type: {type(sum_val)}, value type: {type(sum_val[0])}')
print('sum_val:\n', sum_val)  # 4채널로 반환됨
print('mean_val1:\n', mean_val1)
print('mean_va12:\n', mean_val2)
print()

m1, s1 = cv2.meanStdDev(img) # 원본 영상에 대한 평균과 표준편차
m2, s2 = cv2.meanStdDev(img, mask) # 특정 마스크 영역만 평균과 표준편차
print(f'm1 type: {type(m1)}, value type: {type(m1[0][0])}')
print(f'm1:\n', m1)
print(f'm1_flatten:\n', m1.flatten())
print(f's1:\n', s1)
print(f's1_flatten:\n', s1.flatten())
print()

print(f'm2_flatten:\n', m2.flatten())
print(f's2_flatten:\n', s2.flatten())

cv2.imshow('Origin', img)
cv2.imshow('Mask', mask)
cv2.waitKey(0)

