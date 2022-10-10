import cv2
import numpy as np
import matplotlib.pyplot as plt

def search_value_idx(hist, bias=0):
    for i in range(hist.shape[0]): # 0 ~ 63(64-1)까지 순회
        idx = np.abs(bias - i)     # 검색 위치(처음 혹은 마지막)
        if hist[idx] > 0: # 해당 검색 위치에 빈도가 있으면
            return idx    # 최저 혹은 최대
    return -1

img = cv2.imread('ocean.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

img = cv2.add(img, 100) # 영상 어둡게 해서 분포를 조금 치우치게 함

histSize, ranges = 64, [0, 256]
hist = cv2.calcHist([img], [0], None, [histSize], ranges)

# 히스토그램에서 빈도 행렬에 빈도값이 있는 최저 위치(low), 회고 위치(high) 찾기
bin_width = ranges[1] / histSize  # 256 / 64 = 4
low_level = search_value_idx(hist, 0)
high_level = search_value_idx(hist, histSize - 1)
low_pixel = low_level * bin_width
high_pixel = high_level * bin_width
# 어느 계급에 속하는가? * bin_width(4) = 실제 픽셀 값
print(f'low_pos:{low_level}, high_pos:{high_level}')
print(f'low_pixel: {low_pixel}, high_pixel: {high_pixel}')

# 스트레칭 수식 적용해서 룩업 테이블 생성
idx = np.arange(0, 256)
idx = (idx - low_pixel)/(high_pixel - low_pixel) * 255
idx[:int(low_pixel)] = 0  # 히스토그램 처음 ~ 최저 위치 부분을 0으로 만든다.
idx[int(high_pixel+1):] = 255 # 히스토그램 최고 위치 부분을 255로 만든다.
print('LUT:\n', {i: v for i, v in enumerate(idx)})

dst = cv2.LUT(img, idx.astype('uint8')) # 룩업 테이블 적용
# 아래 코드는 룩업 테이블 사용않고 구현
# dst = np.zeros(img.shape, dtype=img.dtype)
# for i in range(dst.shape[0]):
#    for j in range(dst.shape[1]):
#        dst[i, j] = idx[img[i, j]]

#hist_dst = cv2.calcHist([dst], [0], None, [histSize], ranges) # 결과 히스토그램
#print(dst)

cv2.imshow('Origin', img)
cv2.imshow('Stretching', dst)

plt.subplots(2, 1, constrained_layout=True)
plt.suptitle('Result')

plt.subplot(2, 1, 1)
plt.title('Original image histogram')
plt.hist(img.ravel(), bins=histSize, range=ranges)

plt.subplot(2, 1, 2)
plt.title('Histogram stretching')
plt.hist(dst.ravel(), bins=histSize, range=ranges)
plt.show()

cv2.waitKey(0)