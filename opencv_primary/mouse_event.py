import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누름")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")
    elif event == cv2.EVENT_MOUSEWHEEL:
        print("마우스 휠")

cv2.imshow("Window 1", np.zeros((200, 200))) # 0으로 채워진(검은색) 200x200 행렬
cv2.imshow("Window 2", np.full((200, 200), 255, np.uint8)) # 255로 채워진(흰색) 200x200 행렬

cv2.setMouseCallback("Window 1", onMouse) # Window 1에 대해서만 마우스 이벤트 부여
cv2.waitKey(0) # 키보드 입력 무한대기
cv2.destroyAllWindows()