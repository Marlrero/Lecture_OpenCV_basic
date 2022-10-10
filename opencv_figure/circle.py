import numpy as np
import cv2

image = np.full((400, 500, 3), 255, np.uint8)  # 400x300x3의 흰색 영상

orange, yellow, cyan = (0, 165, 255), (0, 255, 255), (255, 255, 0)
center = (image.shape[1]//2, image.shape[0]//2)  # 영상의 중심 좌표(y, x)
p1, p2 = (300, 200), (100, 200)

cv2.circle(image, center, 100, orange)
cv2.circle(image, p1, 50, yellow, 2)
cv2.circle(image, p2, 70, cyan, -1) # 원 내부 색상 채움(-1)

cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()