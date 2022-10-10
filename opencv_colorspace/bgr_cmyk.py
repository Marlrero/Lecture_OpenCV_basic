import cv2
import numpy as np

bgr_img = cv2.imread('pencils.jpg', cv2.IMREAD_COLOR)
if bgr_img is None: raise Exception('영상 읽기 오류')

white_img = np.array([255, 255, 255], np.uint8)
cmy_img = white_img - bgr_img  # 각 채널에서 255를 뺌 (반전)
cmy = cv2.split(cmy_img) # 채널 분리

black = cv2.min(cmy[0], cv2.min(cmy[1], cmy[2]))
# 최솟값 함수를 두번 사용해 min(cyan, magenta, yellow) 계산
yellow, magenta, cyan = cmy - black

cv2.imshow('black', black)
cv2.imshow('yellow', yellow)
cv2.imshow('magenta', magenta)
cv2.imshow('cyan', cyan)
cv2.waitKey(0)