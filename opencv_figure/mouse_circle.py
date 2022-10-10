import numpy as np
import cv2

title = "Paint"
p = (-1, -1)  # 시작 좌표

def onMouse(event, x, y, flags, param):
    global title, p

    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼을 누르면
        if p[0] < 0:  # 시작 좌표가 -1일 경우
            p = (x, y)  # 현재 마우스 위치로 바꿈
        else: # 시작 좌표가 있을 경우
            cv2.rectangle(image, p, (x, y), (255, 0, 0), 2)
            # 시작 좌표에서 현재 좌표까지 파란색 사각형 그리기 (굵기 2)
            cv2.imshow(title, image) # 이미지 다시 보여주기
            p = (-1, -1)  # 시작 좌표 초기화
    elif event == cv2.EVENT_RBUTTONDOWN: # 오른쪽 버튼을 누르면
        if p[0] < 0:  # 시작 좌표가 -1일 경우
            p = (x, y)  # 현재 마우스 위치로 바꿈
        else: # 시작 좌표가 있을 경우
            dx, dy = p[0] - x, p[1] - y  # 시작좌표와 현재좌표의 간격 구하기
            radius = int(np.sqrt(dx**2 + dy**2)) # 시작좌표와 현재좌표의 거리

            cv2.circle(image, p, radius, (0, 255, 0), 2) # 초록색 원 그리기
            cv2.imshow(title, image) # 이미지 다시 보여주기
            p = (-1, -1)  # 시작 좌표 초기화

image = np.full((400, 500, 3), 255, np.uint8)  # 400x300x3의 흰색 영상

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()