import cv2
import numpy as np

img1 = cv2.imread('moving_1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('moving_2.jpg', cv2.IMREAD_COLOR)
if img1 is None or img2 is None: raise Exception('영상 오픈 오류')

# 원소간 뺄셈
subtract_img1 = cv2.subtract(img1, img2)
# integer16으로 변경해서 뺄셈 (음수값 보존)
subtract_img2 = cv2.subtract(np.int16(img1), np.int16(img2))
abs_img1 = np.absolute(subtract_img2).astype('uint8') # 음수 값을 보존한 상태로 절댓값 후 uint8 변경
abs_img2 = cv2.absdiff(img1, img2) # 음수 값 보존 없이 절댓값으로 변경

cv2.imshow('origin_img1', img1)
cv2.imshow('origin_img2', img2)
cv2.imshow('subtract_img1', subtract_img1)
cv2.imshow('subtract_img2', subtract_img2)
cv2.imshow('abs_img1', abs_img1)
cv2.imshow('abs_img2', abs_img2)
cv2.waitKey(0)