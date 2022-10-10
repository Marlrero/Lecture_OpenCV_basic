import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_hist_opencv(hist, figSize=(200, 256)):
    graph_img = np.full(figSize, 255, np.uint8) # figSize만큼 흰색 영상 생성
    cv2.normalize(hist, hist, 0, figSize[0], cv2.NORM_MINMAX)
       # 최소-최대 정규화 (최소는 0, 최대는 그래프 그림 사이즈 200(y축)까지 최대)
    gap = graph_img.shape[1] / hist.shape[0]
       # 계급의 너비, 그래프 그림 사이즈 256(x축) / 히스토그램(1D) 크기

    for i, h in enumerate(hist): # i는 히스토그램(1D) 크기, h는 그 값
        x = int(round(i * gap)) # 시작 좌표 (x, 0)
        w = int(round(gap))     # gap만큼 width
        cv2.rectangle(graph_img, (x, 0, w, int(h)), 0, cv2.FILLED)

    return cv2.flip(graph_img, 0) # 그림 상하반전(0), 1의 경우 좌우반전

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

cv2.imshow('Image', img)
histSize, ranges = 32, [0, 256] # 히스토그램 간격 수, 값의 범위

# OpenCV로 계산 후, OpenCV로 그리기
hist = cv2.calcHist([img], [0], None, [histSize], ranges)
hist_img = draw_hist_opencv(hist)
cv2.imshow('Histogram image', hist_img)

# matplotlib로 바로 그리기
#plt.hist(img.ravel(), bins=256, range=ranges)
plt.hist(img.ravel(), bins=histSize, range=ranges)
# ravel 함수는 다차원을 1차원으로 -> 복사되지 않고 자체를 변경
# flatten 함수는 다차원을 1차원으로 -> 복사본 반환
# reshape 함수는 원하는 차원으로 -> 복사되지 않고 자체를 변경
plt.show()

cv2.waitKey(0)