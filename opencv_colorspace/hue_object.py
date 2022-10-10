import cv2
import numpy as np

def proc_threshold(value):
    thresh[0] = cv2.getTrackbarPos('Hue_th1', 'result')
    thresh[1] = cv2.getTrackbarPos('Hue_th2', 'result')

    # 화소에 직접 접근해서 이진화
    # result = np.zeros(hue.shape, np.uint8)
    # for i in range(result.reshape[0]):
    #   for j in range(result.reshape[1]):
    #       if thresh[0] <= hue[i, j] < thresh[1]:
    #           result[i, j] = 255

    # 넘파이 함수를 이용해서 이진화
    # result = np.logical_and(hue < thresh[1], hue >= thresh[0]) # 논리 곱
    # result = result.astype('uint8') * 255

    # OpenCV 이진화
    _, result = cv2.threshold(hue, thresh[1], 255, cv2.THRESH_TOZERO_INV)
    # cv2.THRESH_TOZERO_INV: thresh[1] 이상의 값은 0으로, 이하의 값은 그대로 가져옴
    cv2.threshold(result, thresh[0], 255, cv2.THRESH_BINARY, result)
    # cv2.THRESH_BINARY: thresh[0] 이하의 값은 0으로, 이상은 255로 지정
    cv2.imshow('result', result)

bgr_img = cv2.imread('monkey.jpg', cv2.IMREAD_COLOR)
if bgr_img is None: raise Exception('영상 읽기 에러')

hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
hue = np.copy(hsv_img[:, :, 0]) # hue 행렬에 색상 채널 복사

thresh = [50, 100]
cv2.namedWindow('result')
# trackbarname, winname, value, count, onChange
cv2.createTrackbar('Hue_th1', 'result', thresh[0], 255, proc_threshold)
cv2.createTrackbar('Hue_th2', 'result', thresh[1], 255, proc_threshold)
proc_threshold(thresh[0])
cv2.imshow('bgr_img', bgr_img)
cv2.waitKey(0)

