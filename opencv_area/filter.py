import cv2
import numpy as np

# 행렬 처리 방식 (속도가 빠름)
def mat_filter(img, mask):
    rows, cols = img.shape[:2]
    #print(rows, cols)
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask.shape[1] // 2, mask.shape[0] // 2 # 마스크 중심

    # print(ycenter, rows - ycenter)
    # print(xcenter, cols - xcenter)
    for i in range(ycenter, rows - ycenter):  # 영상의 끝 상하부분 제외
        for j in range(xcenter, cols - xcenter): # 영상의 끝 좌우부분 제외
            y1, y2 = i - ycenter, i + ycenter + 1 # 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1 # 너비 범위
            roi = img[y1:y2, x1:x2].astype('float32') # 관심 영역 float32 변환
            mul = cv2.multiply(roi, mask) # 관심영역과 마스크 원소별 곱(컨볼루션)
            dst[i, j] = cv2.sumElems(mul)[0] # 원소별로 곱한 것을 다시 합해서(컨볼루션)저장
            # 단일 채널이기 때문에 0번째만 가져옴

    return dst