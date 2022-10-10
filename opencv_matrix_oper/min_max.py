import cv2
import numpy as np

data = [1, 400, 320, 8, 0,
        21, 23, 57, 20, 11,
        30, 39, 84, 72, 12] # 1D 리스트
a = np.reshape(data, (3, 5)) # 1D 리스트 -> 3x5 행렬
b = np.full((3, 5), 20)  # 원소값이 20인 3x5 행렬

min_a = cv2.min(a, 50) # 스칼라와 비교해서 최솟값 넣기
max_a = cv2.max(a, b)  # a와 b 비교해서 최댓값 넣기
print('min_a:\n', min_a)
print('max_a:\n', max_a)
print()

print('a:\n', a)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(a)
print(f'최솟값: {min_val}-{min_loc}\n최댓값: {max_val}-{max_loc}')

img = cv2.imread('forest.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상파일 읽기 에러')

min_val, max_val, _, _ = cv2.minMaxLoc(img) # 영상에서 최솟값 최댓값만 가져옴
print(f'원본이미지 최솟값={min_val}, 최댓갑={max_val}')

ratio = 255 / (max_val - min_val) # min-max하고 최대 밝기인 255로 나눔
output = np.round((img - min_val) * ratio).astype('uint8')
 # 영상 픽셀에 픽셀 최솟값을 빼고 ratio를 곱함 -> 영상 픽셀 최솟값이 0에서 최댓값 255가 됨
min_val, max_val, _, _ = cv2.minMaxLoc(output) # output 영상에서 최솟값 최댓값만 가져옴
print(f'보정이미지 최솟값={min_val}, 최댓갑={max_val}')

cv2.imshow('origin', img)
cv2.imshow('output', output)
cv2.waitKey(0)