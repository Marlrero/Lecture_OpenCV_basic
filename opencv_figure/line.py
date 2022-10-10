import numpy as np
import cv2

image = np.full((400, 500, 3), 255, np.uint8)  # 400x300x3의 흰색 영상

cv2.line(image, (50, 50), (200, 100), (0, 0, 255)) # (50, 50) -red-> (200, 100)
cv2.line(image, (200, 300), (400, 100), (255, 0, 0), 10, cv2.LINE_AA)
  # (200, 300) -blue-> (400, 100), 굵기 10, 계단현상감소 선

cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()