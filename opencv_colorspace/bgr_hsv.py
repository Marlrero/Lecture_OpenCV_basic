import cv2
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

def convert_hsi(bgr):
    # b, g, r을 float로 변환
    #b, g, r = bgr.astype(float)
    b, g, r = float(bgr[0]), float(bgr[1]), float(bgr[2])
    bgr_sum = (b + g + r)

    a = ((r - g) + (r - b)) * 0.5
    b = math.sqrt(((r - g) ** 2) + (r - b) * (g - b))
    theta = math.acos(a / b) * (180 / np.pi) if b else 0
    # theta를 radian에서 degree로 변환하는 것임 (만약 b가 0일 경우에는 0 degree)

    h = theta if b <= g else 360 - theta
    s = 1.0 - (3.0 * min([r, g, b]) / bgr_sum if bgr_sum else 0)
    i = bgr_sum / 3.0

    # h는 0 ~ 360도를 가지므로, uint8이 0 ~ 255 범위이기 때문에
    #    절반으로 스케일을 줄여 0 ~ 180 범위로 변경함
    # s는 0 ~ 1의 값을 가지므로 255를 곱해서 0 ~ 255 범위를 갖게 함
    return (h / 2, s * 255, i)

def bgr2hsi(img): # bgr -> hsi 컬러 변환
    hsi = [[convert_hsi(pixel) for pixel in row] for row in img] # 2차원 배열 순회
    # convertScaleAbs : 값을 절댓값으로 바꾸고 정수(unsigned 8bit integer)로 바꿔주는 함수
    return cv2.convertScaleAbs(np.array(hsi))

bgr_img = cv2.imread('pencils.jpg', cv2.IMREAD_COLOR)
if bgr_img is None: raise Exception('영상 읽기 에러')

hsi_img = bgr2hsi(bgr_img) # 직접 만든 함수 사용
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV) # OpenCV 함수 사용

hue, saturation, intensity = cv2.split(hsi_img)
hue2, saturation2, intensity2 = cv2.split(hsv_img)

cv2.imshow('Direct hue', hue)
cv2.imshow('Direct saturation', saturation)
cv2.imshow('Direct intensity', intensity)
cv2.imshow('OpenCV hue', hue2)
cv2.imshow('OpenCV saturation', saturation2)
cv2.imshow('OpenCV intensity', intensity2)

'''
plt.subplots(2, 1, constrained_layout=True)
plt.suptitle('Result')

plt.subplot(2, 1, 1)
plt.title('Direct histogram')
plt.hist(hue.ravel(), bins=180, range=[0, 181]) # hsi_img.reshape(-1)

plt.subplot(2, 1, 2)
plt.title('OpenCV histogram')
plt.hist(hue2.ravel(), bins=180, range=[0, 181]) # hsv_img.reshape(-1)
plt.show()
'''
cv2.waitKey(0)

