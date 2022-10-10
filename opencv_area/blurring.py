import cv2
import numpy as np

# 행렬 처리 방식 (속도가 빠름)
def mat_filter(img, mask):
    rows, cols = img.shape[:2]
    print(rows, cols)
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

# 화소 처리 방식 (속도가 느림)
def pix_filter(img, mask):
    rows, cols = img.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask.shape[1] // 2, mask.shape[0] // 2  # 마스크 중심

    for i in range(ycenter, rows - ycenter):  # 영상의 끝 상하부분 제외
        for j in range(xcenter, cols - xcenter):  # 영상의 끝 좌우부분 제외
            sum = 0.0
            for u in range(mask.shape[0]):  # 마스크 행 반복
                for v in range(mask.shape[1]): # 마스크 열 반복
                    # 마스크 범위의 입력 화소 y, x 계산
                    y, x = i + u - ycenter, j + v - xcenter
                    sum += img[y, x] * mask[u, v] # 컨볼루션

            dst[i, j] = sum

    return dst

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception('영상 읽기 에러')

kernel = [
    1/9, 1/9, 1/9,
    1/9, 1/9, 1/9,
    1/9, 1/9, 1/9
]
kernel = np.array(kernel, np.float32).reshape(3, 3) # 커널(마스크) 생성
blur1 = mat_filter(img, kernel)
blur2 = pix_filter(img, kernel)

blur1 = blur1.astype('uint8') # 영상으로 표현하기 위해 uint8로 변경
blur2 = cv2.convertScaleAbs(blur2) # 영상으로 표현하기 위해 OpenCV 함수 사용
# 값을 절댓값으로 바꾸고 unsigned 8bit integer로 변경하는 함수

cv2.imshow('origin', img)
cv2.imshow('matrix blur', blur1)
cv2.imshow('pixel blur', blur2)
cv2.waitKey(0)