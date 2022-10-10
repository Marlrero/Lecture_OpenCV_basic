import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('ocean.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

histSize, ranges = 256, [0, 256]
hist = cv2.calcHist([img], [0], None, [histSize], ranges)
#print('hist.shape:', hist.shape)

# 직접 누적합 구현
accum_hist = np.zeros(hist.shape[:2], np.float32) # 빈 배열 생성(누적합)
accum_hist[0] = hist[0]  # 누적 히스토그램의 첫번째 값은 원래 히스토그램의 첫번째 값
for i in range(1, hist.shape[0]):  # 1 ~ 255까지
    accum_hist[i] = accum_hist[i - 1] + hist[i]

print('accum_hist:\n', accum_hist.ravel())
accum_hist = (accum_hist / sum(hist)) * 255 # 누적합 정규화
print('accum_hist_normalize:\n', {i: v for i, v in enumerate(accum_hist)})
dst1 = [[accum_hist[val] for val in row] for row in img]
dst1 = np.array(dst1, np.uint8) # float32를 uint8로 변경

# 직접 누적합 구현 - LUT 사용방법
accum_hist_np = np.cumsum(hist) # numpy 누적합 계산 함수
#print('accum_hist_np:\n', accum_hist_np)
cv2.normalize(accum_hist_np, accum_hist_np, 0, 255, cv2.NORM_MINMAX)  # 정규화
dst2 = cv2.LUT(img, accum_hist_np.astype('uint8'))

# OpenCV 함수로
dst3 = cv2.equalizeHist(img)

cv2.imshow('Origin', img)
cv2.imshow('Equalization - Direct', dst1)
cv2.imshow('Equalization - Direct LUT', dst2)
cv2.imshow('Equalization - OpenCV', dst3)

plt.subplots(2, 2, constrained_layout=True)
plt.suptitle('Result')

plt.subplot(2, 2, 1)
plt.title('Original image histogram')
plt.hist(img.ravel(), bins=histSize, range=ranges)

plt.subplot(2, 2, 2)
plt.title('Equalize Direct')
plt.hist(dst1.ravel(), bins=histSize, range=ranges)

plt.subplot(2, 2, 3)
plt.title('Equalize Direct LUT')
plt.hist(dst2.ravel(), bins=histSize, range=ranges)

plt.subplot(2, 2, 4)
plt.title('Equalize OpenCV')
plt.hist(dst3.ravel(), bins=histSize, range=ranges)
plt.show()

cv2.waitKey(0)