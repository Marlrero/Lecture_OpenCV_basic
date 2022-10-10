import cv2
import numpy as np

def minmax_filter(image, ksize, mode):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8) # 결과
    center = ksize // 2  # 마스크 절반 크기

    # 3x3 마스크 크기라면 상하좌우 1픽셀을 제외함
    # 5x5 마스크 크기라면 상하좌우 2픽셀을 제외함
    for i in range(center, rows - center):  # 입력 영상 순회
        for j in range(center, cols - center):
            # 마스크 영역 행렬 처리 방식
            y1, y2 = i - center, i + center + 1  # 마스크 높이 범위
            x1, x2 = j - center, j + center + 1  # 마스크 너비 범위
            mask = image[y1:y2, x1:x2]  # 마스크 영역
            dst[i, j] = cv2.minMaxLoc(mask)[mode] # [0]은 최소, [1]은 최대
            # 최솟값, 최댓값, 최솟값좌표, 최댓값좌표로 4개가 반환됨

    return dst

img = cv2.imread("mountain.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상파일 읽기 오류")
'''
img = np.array([
    [50, 60, 90, 50, 100],
    [100, 90, 200, 50, 30],
    [100, 100, 100, 200, 100],
    [100, 100, 150, 150, 50],
    [30, 90, 80, 70, 160]
], np.uint8)
'''

minfilter_img = minmax_filter(img, 3, 0)  # 3x3 마스크 최솟값 필터링
maxfilter_img = minmax_filter(img, 3, 1)  # 3x3 마스크 최댓값 필터링
print(minfilter_img)
print(maxfilter_img)

cv2.imshow("image", img)
cv2.imshow("minfilter_img", minfilter_img)
cv2.imshow("maxfilter_img", maxfilter_img)
cv2.waitKey(0)