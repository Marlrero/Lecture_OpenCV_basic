import numpy as np
import cv2

image = np.full((400, 500, 3), 255, np.uint8)  # 400x300x3의 흰색 영상

black = (0, 0, 0)
cv2.putText(image, "SIMPLEX", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, black)
cv2.putText(image, "DUPLEX", (100, 180), cv2.FONT_HERSHEY_DUPLEX, 2, black)
cv2.putText(image, "TRIPLEX", (100, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, black)
font = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC  # 비트 OR 연산자로 여러 폰트 적용 가능
cv2.putText(image, "ITALIC", (100, 340), font, 2, black)

cv2.imshow("Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()