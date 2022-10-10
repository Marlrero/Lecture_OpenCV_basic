import cv2
import numpy as np

img1 = np.zeros((300, 300), np.uint8) # 300x300의 검은색(0) 영상
img2 = img1.copy() # img1 영상을 복사

height, width = img1.shape        # 세로 길이, 가로 길이
cx, cy = width // 2, height // 2  # 중심점
# img1에 중심좌표(cx, cy), 반지름 100, 흰색(255), 선 두께 없음(-1) 원
cv2.circle(img1, (cx, cy), 100, 255, -1)
# img2에 왼쪽상단(0, 0), 오른쪽하단(cx, height), 흰색(255), 선 두께 없음(-1) 사각형
# 원점부터 x축의 절반 y축 맨 끝까지 그리는 것임 -> 반절 사각형
cv2.rectangle(img2, (0, 0, cx, height), 255, -1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('AND', cv2.bitwise_and(img1, img2))
cv2.imshow('OR', cv2.bitwise_or(img1, img2))
cv2.imshow('XOR', cv2.bitwise_xor(img1, img2))
cv2.imshow('NOT', cv2.bitwise_not(img1))
cv2.waitKey(0)