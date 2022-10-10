import cv2

img = cv2.imread('fabric.jpg', cv2.IMREAD_COLOR)
if img is None:
    raise Exception('영상파일 열기 실패')
if img.ndim != 3:
    raise Exception('영상파일이 3채널, 컬러가 아님')

bgr = cv2.split(img) # BGR 채널 각 채널로 분리
print('bgr type:', type(bgr), type(bgr[0]), type(bgr[0][0][0]))
  # bgr의 자료형, bgr[0](단일채널) 자료형, bgr[0]의 원소 자료형(실제 픽셀값)
print('bgr #:', len(bgr)) # 3채널이니, 3개임

cv2.imshow('Origin', img)
cv2.imshow('Blue', bgr[0]) # or cv2.imshow('Blue', img[:, :, 0]
cv2.imshow('Green', bgr[1])
cv2.imshow('Red', bgr[2])
cv2.waitKey(0)