import cv2
import numpy as np

img = np.arange(10).reshape(2, 5) # 0 ~ 9까지 원소로 구성된 2x5 행렬
print('img:\n', img) # 행렬의 값이 곧, 픽셀(화소) 값

# numpy array 이용 방식 1
for i in range(img.shape[0]): # 행 접근 (2번 반복)
    for j in range(img.shape[1]): # 열 접근 (5번 반복)
        img[i, j] = 255 - img[i, j]  # 화소 접근과 할당
'''
# numpy array 이용 방식 2
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img.itemset((i, j),  255 - img.item(i, j))  # 화소 접근과 할당

# numpy array 이용 방식 3
img = 255 - img  # numpy ndarray 간에 산술 연산을 이용

# lookup table(lut) 이용 방식
lut = np.array([255 - i for i in range(256)], np.uint8)
print('lut:\n', lut)
img = lut[img]

# OpenCV 함수 방식
img = cv2.subtract(255, img)
'''
print('img_-255:\n', img)