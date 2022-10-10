import cv2
import numpy as np

bgr_img = cv2.imread('pencils.jpg', cv2.IMREAD_COLOR)
if bgr_img is None: raise Exception('영상 읽기 오류')

white_img = np.array([255, 255, 255], np.uint8)
cmy_img = white_img - bgr_img  # 각 채널에서 255를 뺌 (반전)
yellow, magenta, cyan = cv2.split(cmy_img) # 채널 분리

cv2.imshow('bgr_img', bgr_img)
cv2.imshow('cmy_img', cmy_img)
cv2.imshow('yellow', yellow)
cv2.imshow('magenta', magenta)
cv2.imshow('cyan', cyan)
cv2.waitKey(0)