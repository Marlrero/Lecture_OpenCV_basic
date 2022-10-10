import cv2

img = cv2.imread('pyramid.jpg', cv2.IMREAD_COLOR)
if img is None:
    raise Exception('영상파일 열기 실패')

rep = cv2.repeat(img, 1, 2) # 세로 방향 1번, 수평 방향 2번 반복

cv2.imshow('repeat', rep)
cv2.waitKey(0)