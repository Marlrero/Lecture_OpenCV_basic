import cv2
import numpy as np

def erode(img, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8) # 마스크가 없으면 생성
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0] # 마스크 중심 좌표 (몫=[0])

    is_non_zero = cv2.countNonZero(mask) # 마스크에서 원소값이 0이 아닌 원소 개수 계산
    for i in range(ycenter, img.shape[0] - ycenter): # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1  # 마스크 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1  # 마스크 너비 범위
            roi = img[y1:y2, x1:x2]                # 마스크 영역
            temp = cv2.bitwise_and(roi, mask) # 마스크의 1인 원소 and 관심 영역 1(255)이면 1
            cnt  =  cv2.countNonZero(temp)  # 일치한 화소수 계산
            dst[i, j] = 255 if (cnt == is_non_zero) else 0  # 출력 화소에 저장
            # 마스크의 1인 원소 개수와 논리곱 행렬의 1인 원소 개수 비교 (같으면 모두 일치이므로 255)
    return dst

def dilate(img, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8) # 마스크가 없으면 생성
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0] # 마스크 중심 좌표 (몫=[0])

    #is_non_zero = cv2.countNonZero(mask) # 마스크에서 원소값이 0이 아닌 원소 개수 계산
    for i in range(ycenter, img.shape[0] - ycenter): # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1  # 마스크 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1  # 마스크 너비 범위
            roi = img[y1:y2, x1:x2]                # 마스크 영역
            temp = cv2.bitwise_and(roi, mask) # 마스크의 1인 원소 and 관심 영역 1(255)이면 1
            cnt  =  cv2.countNonZero(temp)  # 일치한 화소수 계산
            #dst[i, j] = 255 if (cnt == is_non_zero) else 0  # 출력 화소에 저장
            # 마스크의 1인 원소 개수와 논리곱 행렬의 1인 원소 개수 비교 (같으면 모두 일치이므로 255)
            dst[i, j] = 0 if (cnt == 0) else 255 # cnt가 0이면 모든 원소 불일치이므로 0
    return dst