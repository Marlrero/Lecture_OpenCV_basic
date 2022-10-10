import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Origin', img)

# OpenCV 함수 이용 (saturation)
r1 = cv2.add(img, 100)  # 영상 밝게
r2 = cv2.subtract(img, 100) # 영상 어둡게

cv2.imshow('Origin', img)
cv2.imshow('bright', r1)
cv2.imshow('dark', r2)

histSize, ranges = 32, [0, 256] # 히스토그램 간격 수, 값의 범위

plt.title('Original image histogram')
plt.hist(img.ravel(), bins=histSize, range=ranges)

plt.subplots(1, 2, constrained_layout=True) # 서브플롯 간의 간격을 최적의 수치로
plt.suptitle('Histogram')

plt.subplot(1, 2, 1)
plt.title('bright')
plt.hist(r1.ravel(), bins=histSize, range=ranges)

plt.subplot(1, 2, 2)
plt.title('dark')
plt.hist(r2.ravel(), bins=histSize, range=ranges)
plt.show()

cv2.waitKey(0)