import numpy as np
import cv2

# 0으로 초기화된 400x300 행렬 생성. 타입은 unsigned integer 8bit
# uint8을 한 이유는 2^8 = 256, 0 ~ 255까지의 색상 표현이 가능
image = np.zeros((400, 300), np.uint8)
image[:] = 200  # 밝은 회색(200)으로 행렬 값(픽셀) 모두 변경

win_name1 = "window1"
win_name2 = "window2"

cv2.namedWindow(win_name1, cv2.WINDOW_AUTOSIZE) # 행렬에 맞게 조정(크기변경불가)
cv2.namedWindow(win_name2, cv2.WINDOW_NORMAL) # 크기변경가능

cv2.moveWindow(win_name1, 100, 100) # 모니터 (100, 100) 위치에 지정
cv2.moveWindow(win_name2, 400, 400) # 모니터 (400, 400) 위치에 지정

cv2.imshow(win_name1, image)
cv2.imshow(win_name2, image) # 밝은회색 이미지를 윈도우에 붙이기
cv2.waitKey(0) # 키보드 입력 대기
cv2.destroyAllWindows()