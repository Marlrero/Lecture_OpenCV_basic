import numpy as np
import cv2

image = np.zeros((300, 300), np.uint8)
window_name = "Trackbar Window"
trackbar_name = "Brightness"

def onChange(pos):
    global image, window_name

    add_color = pos - int(image[0][0])
    image += np.array([add_color], np.uint8)
    cv2.imshow(window_name, image)

def onMouse(event, x, y, flags, param):
    global image, trackbar_name, window_name

    if event == cv2.EVENT_MOUSEWHEEL:
        current_pos = cv2.getTrackbarPos(trackbar_name, window_name)
        if current_pos < 255 and flags > 0:  # flags > 0이면 스크롤 업
            cv2.setTrackbarPos(trackbar_name, window_name, current_pos + 1)
        elif current_pos > 0 and flags < 0:  # flags < 0이면 스크롤 다운
            cv2.setTrackbarPos(trackbar_name, window_name, current_pos - 1)


cv2.imshow(window_name, image)

cv2.createTrackbar(trackbar_name, window_name, image[0][0], 255, onChange)
cv2.setMouseCallback(window_name, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()