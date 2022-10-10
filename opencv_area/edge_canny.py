import cv2
import numpy as np

def non_maximum_suppression(sobel, gradient4):
    rows, cols = sobel.shape[:2] # 소벨 마스크의 가로, 세로 크기
    dst = np.zeros((rows, cols), np.float32) # 최종 결과(소벨 마스크 크기와 같음)

    # 3x3 소벨 마스크라면 반복 1번되는 것임
    for i in range(1, rows - 1): # 1 ~ 소벨 마스크 - 1까지 (양 끝 제외)
        for j in range(1, cols - 1):
            # 행렬 처리로 중심 에지 주변 9개 화소 가져오기
            roi = sobel[i - 1:i + 2, j - 1: j + 2].flatten()
            first_neighbor = [3, 0, 1, 2] # 첫 이웃화소 좌표 4개(0, 45, 90. 135)
            pos = first_neighbor[gradient4[i, j]] # 방향에 따른 첫 이웃화소 위치
            v1, v2 = roi[pos], roi[8 - pos] # 두 이웃 화소를 가져오기

            # if문으로 중심 에지 주변 9개 화소 가져오기
            # if gradient4[i, j] == 0: # 기울기 방향이 0도 라면
            #   v1, v2 = sobel[i, j - 1], sobel[i, j + 1]
            # 위와 같이 45도, 90도, 135도를 구성할 수도 있음

            dst[i, j] = sobel[i, j] if (v1 < sobel[i, j] > v2) else 0 # 비최대치 억제

    return dst

def trace(max_sobel, i, j, low): # 에지 추적
    h, w = max_sobel.shape  # 비최대치 억제한 결과 배열 크기
    if (0 <= i < h and 0 <= j < w) == False: # 추적할 화소 범위안에 없다면
        return # 추적 종료

    # 추적 완료 점검 행렬에서 아직 추적안하고, 비최대치 억제 결과 배열이 임계값 low보다 크다면
    if pos_check[i, j] == 0 and max_sobel[i, j] > low:
        pos_check[i, j] = 255 # 추적 완료했다고 표시
        canny[i, j] = 255 # 에지로 지정함

        trace(max_sobel, i - 1, j - 1, low) # 재귀 호출(8방향 추적)
        trace(max_sobel, i, j - 1, low)
        trace(max_sobel, i + 1, j - 1, low)
        trace(max_sobel, i - 1, j, low)
        trace(max_sobel, i + 1, j, low)
        trace(max_sobel, i - 1, j + 1, low)
        trace(max_sobel, i, j + 1, low)
        trace(max_sobel, i + 1, j + 1, low)

def hysteresis_thresholding(max_sobel, low, high): # 이력 임계 처리
    rows, cols = max_sobel.shape[:2]
    for i in range(1, rows - 1): # 에지 영상 순회
        for j in range(1, cols - 1):
            if max_sobel[i, j] >= high: # 각 화소에서 high보다 크면 에지 추적 시작
                trace(max_sobel, i, j, low)

img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.resize(img, dsize=(400, 500), interpolation=cv2.INTER_CUBIC)
if img is None: raise Exception('영상 읽기 에러')

pos_check = np.zeros(img.shape[:2], np.uint8) # 추적 완료 점검 행렬
canny = np.zeros(img.shape[:2], np.uint8) # 캐니 에지 행렬

# 가우시안 블러링 적용
gaus_img = cv2.GaussianBlur(img, (5, 5), 0.3) # 5x5로 가우시안 블러링 (표준편차 0.3)
Gx = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 1, 0, 3) # x방향 sobel 3x3 마스크
Gy = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 0, 1, 3) # y방향 sobel 3x3 마스크
sobel = np.fabs(Gx) + np.fabs(Gy) # 두 행렬의 절댓값으로 덧셈 (크기)
#sobel = cv2.magnitude(Gx, Gy) # x방향 기울기와 y방향 기울기의 강도(두 행렬의 크기)
 # magnitude 함수는 제곱해서 루트를 씌우는 형태로 계산

gradient = cv2.phase(Gx, Gy) / (np.pi / 4)
  # Gx와 Gy간의 각도(라디안) -> 45간격 근사이므로 pi/4
gradient = gradient.astype(int) % 4
  # 각도를 정수로 바꾸고, 8개 값으로 근사된 각도를 0 ~ 3의 값을 가지도록 변경
  # 0, 180 = 0 / 45, 225 = 1 / 90, 270 = 2 / 135, 315 = 3
max_sobel = non_maximum_suppression(sobel, gradient)
hysteresis_thresholding(max_sobel, 100, 150) # low = 100, high = 150

# OpenCV 함수로 사용
canny2 = cv2.Canny(img, 100, 150) # low = 100, high = 150

cv2.imshow('origin', img)
cv2.imshow('canny', canny)
cv2.imshow('OpenCV canny', canny2)
cv2.waitKey(0)