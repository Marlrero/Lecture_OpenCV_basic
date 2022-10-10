import cv2
import numpy as np

# 행렬(이미지)의 1차원 히스토그램을 계산하는 함수를 직접 코드로
def get_histogram(image, histSize, range=[0, 256]):
    hist = np.zeros((histSize, 1), np.float32) # histSize x 1만큼 값이 0인 1D 행렬
    gap = range[1] / histSize # 계급사이 간격

    for row in image:  # 이미지에서 행 순회
        for pixel in row:  # 행 안에서 픽셀 순회
            hist[int(pixel / gap)] += 1
            # 현재 픽셀 값을 계급 사이 간격으로 나눠서 hist[계급]에서 1 증가

    return hist

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

histSize, ranges = 32, [0, 256] # 히스토그램 간격 수, 값의 범위
gap = ranges[1] / histSize     # 256 / 32 = 8의 계급 간격
n_gap = np.arange(0, ranges[1] + 1, gap) # numpy 계급 범위와 간격
  # 0 ~ 256 + 1, 간격(gap)의 배열 생성 -> +1을 해주는 이유는 cv2.calcHist와 맞추기 위해

h1 = get_histogram(img, histSize, ranges) # 직접 만든 함수 사용
h2 = cv2.calcHist([img], [0], None, [histSize], ranges) # OpenCV 함수 사용
# [img]가 가능한 이유는 calcHist 함수가 여러 개의 행렬(이미지)을 통해 히스토그램을 구할 수 있음
h3, bins = np.histogram(img, n_gap) # numpy 함수 이용

print('직접 구현:\n', h1.flatten()) # 2차원 행렬로 반환되므로 1차원으로 풀어줌
print('OpenCV:\n', h2.flatten()) # 2차원 행렬로 반환되므로 1차원으로 풀어줌
print('Numpy:\n', h3)