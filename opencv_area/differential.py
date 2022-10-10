import cv2
import numpy as np
from filter import mat_filter

def get_differential(img, mask1, mask2):
    kernel1 = np.array(mask1, np.float32).reshape(3, 3)
    kernel2 = np.array(mask2, np.float32).reshape(3, 3)

    dst1 = mat_filter(img, kernel1)
    dst2 = mat_filter(img, kernel2)
    dst = cv2.magnitude(dst1, dst2)

    # 아래 코드는 주석처럼 처리해도 같은 결과임 (아래를 수행하는 것이 cv2.convertScaleAbs)
    # dst1 = np.abs(dst1)
    # dst1 = np.clip(dst1, 0, 255).astype('uint8')
    dst1 = cv2.convertScaleAbs(dst1)
    dst2 = cv2.convertScaleAbs(dst2)
    dst = cv2.convertScaleAbs(dst)

    return dst, dst1, dst2
