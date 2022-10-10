import cv2
import numpy as np

# 자동차 이미지 출처: https://m.carisyou.com/magazine/FOCUS/74536
img = cv2.imread('car_number.jpg', cv2.IMREAD_COLOR)
if img is None: raise Exception('영상 읽기 에러')

mask = np.ones((5, 17), np.uint8) # 닫힘 연산 마스크
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 그레이스케일로 변환
gray = cv2.blur(gray, (5, 5)) # 블러링(평균값 필터링)
gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5) # 소벨 에지 검출(x방향 미분, 5x5)

bi_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1] # 이진화
morph = cv2.morphologyEx(bi_img, cv2.MORPH_CLOSE, mask, iterations=3)
 # 닫힘 연산 수행. 반복 횟수 3번

cv2.imshow('Car image', img)
cv2.imshow('Binary image', bi_img)
cv2.imshow('Closing image', morph)
cv2.waitKey(0)