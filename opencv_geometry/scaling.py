import cv2
import numpy as np
import time

def scaling(img, size):  # 크기 변경 함수(행렬 처리 방식)
    dst = np.zeros(size[::-1], img.dtype)  # size와 shape는 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2]) # size를 역순으로 하여 shape와 나눔
    y = np.arange(0, img.shape[0], 1) # 입력 영상의 세로 범위만큼 좌표 생성 (1씩)
    x = np.arange(0, img.shape[1], 1) # 입력 영상의 가로 범위만큼 좌표 생성 (1씩)
    y, x = np.meshgrid(y, x) # 좌표 y와 x를 통해 정방행렬 생성
    i, j = np.int32(y * ratioY), np.int32(x * ratioX) # 크기 변경 수식
    dst[i, j] = img[y, x] # 이를 행렬에 그대로 복사
    return dst

def scaling2(img, size):  # 크기 변경 함수(반복문 방식)
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):  # 입력 영상 순회 - 순방향 사상
        for x in range(img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)  # 크기 변경 수식
            dst[i, j] = img[y, x]
    return dst

def time_check(func, img, size, title):  ## 수행시간 체크 함수
    start_time = time.perf_counter()
    ret_img = func(img, size)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(f'{title} 수행시간: {elapsed:0.2f} ms')
    return ret_img

img = cv2.imread('baby.jpg', cv2.IMREAD_GRAYSCALE) # 640x476
if img is None: raise Exception("영상 읽기 에러")

dst1 = scaling(img, (300, 200))  # 크기 변경 - 축소
dst2 = scaling2(img, (800, 600))  # 크기 변경 - 확대

# 속도 측정
dst3 = time_check(scaling, img, (800, 600), "행렬 방식>") # 확대
dst4 = time_check(scaling2, img, (800, 600), "반복문 방식>") # 확대

cv2.imshow("image", img)
cv2.imshow("dst1- zoom out", dst1)
cv2.imshow("dst2- zoom in", dst2)
cv2.waitKey(0)