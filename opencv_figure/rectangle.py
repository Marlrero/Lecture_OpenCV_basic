import numpy as np
import cv2

image = np.full((400, 500, 3), 255, np.uint8)  # 400x300x3의 흰색 영상

cv2.rectangle(image, (50, 50), (200, 100), (255, 0, 0), 5, cv2.LINE_4)
cv2.rectangle(image, (100, 200, 150, 150), (0, 0, 0), cv2.FILLED)

cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()