import cv2
import numpy as np

def scaling(img, size):  # 크기 변경(이전 예제)
    dst = np.zeros(size[::-1], img.dtype)  # size와 shape는 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2]) # size를 역순으로 하여 shape와 나눔
    y = np.arange(0, img.shape[0], 1) # 입력 영상의 세로 범위만큼 좌표 생성 (1씩)
    x = np.arange(0, img.shape[1], 1) # 입력 영상의 가로 범위만큼 좌표 생성 (1씩)
    y, x = np.meshgrid(y, x) # 좌표 y와 x를 통해 정방행렬 생성
    i, j = np.int32(y * ratioY), np.int32(x * ratioX) # 크기 변경 수식
    dst[i, j] = img[y, x] # 이를 행렬에 그대로 복사
    return dst

def scaling_nearest(img, size):  # 크기 변경(이웃화소)
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1) # 출력 영상의 세로 범위만큼 좌표 생성 (1씩)
    j = np.arange(0, size[0], 1) # 출력 영상의 가로 범위만큼 좌표 생성 (1씩)
    i, j = np.meshgrid(i, j) # 출력 영상의 좌표를 가지고 정방행렬 생성
    y, x = np.int32(i / ratioY), np.int32(j / ratioX) # 크기 변경 수식 (역방향 사상)
    dst[i, j] = img[y, x] # 이를 행렬에 그대로 복사
    return dst

img = cv2.imread('baby.jpg', cv2.IMREAD_GRAYSCALE) # 640x476
if img is None: raise Exception("영상 읽기 에러")

dst1 = scaling(img, (800, 600))  # 크기 변경 - 축소
dst2 = scaling_nearest(img, (800, 600))  # 크기 변경 - 확대

cv2.imshow("image", img)
cv2.imshow("dst1- scaling", dst1)
cv2.imshow("dst2- nearest", dst2)
cv2.waitKey(0)