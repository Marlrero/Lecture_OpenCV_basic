import numpy as np
import cv2

image = np.zeros((300, 300), np.uint8)  # 0으로 채운(검은색) 300x300 행렬
window_name = "Trackbar Window"

def onChange(pos):  # pos는 17번째 줄에 의해 0 ~ 255 값의 정수가 올 것임.
    global image, window_name  # image, window_name 변수는 바깥(전역, global)에 있음

    add_color = pos - int(image[0][0])
    #image += add_color (이렇게 하면 줄일 때 에러!)
    #줄이면 add_color가 음수가 되고, 이를 uint8(양수만)에 더하려면 타입이 맞지 않음
    #따라서, 이를 uint8로 형변환해야 함
    image += np.array([add_color], np.uint8)    # 스칼라 덧셈 수행
    cv2.imshow(window_name, image)  # 다시 색 변경

cv2.imshow(window_name, image)

# 3번째 입력 image[0][0] -> 0(검은색)을 의미함 -> 이것이 슬라이더 위치 값이 됨
# 4번째 입력 255(흰색)을 의미함 -> 이것이 슬라이더의 최댓값이 됨
# 5번째 입력: 슬라이더 위치가 변경되면 실행되는 함수 이름
cv2.createTrackbar("Brightness", window_name, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()