import cv2
import numpy as np

def average_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8) # 결과
    center = ksize // 2  # 마스크 절반 크기

    for i in range(rows):  # 입력 영상 순회
        for j in range(cols):
            # 마스크 영역 행렬 처리 방식
            y1, y2 = i - center, i + center + 1  # 마스크 높이 범위
            x1, x2 = j - center, j + center + 1  # 마스크 너비 범위

            if y1 < 0 or y2 > rows or x1 < 0 or x2 > cols: # 범위를 벗어나면
                dst[i, j] = image[i, j] # 중심 화소를 출력 화소로 지정함
                # cv2.BORDER_CONSTANT 방식임
            else:
                mask = image[y1:y2, x1:x2]  # 마스크 영역
                dst[i, j] = cv2.mean(mask)[0] # np.mean(mask)도 가능

    return dst

img = cv2.imread("mountain.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상파일 읽기 오류")
'''
img = np.array([
    [50, 60, 90, 50, 100],
    [100, 90, 200, 50, 30],
    [100, 100, 100, 200, 100],
    [100, 100, 150, 150, 50],
    [30, 90, 80, 70, 160]
], np.uint8)
'''

#avg_img = average_filter(img, 3)  # 직접 만든 평균 필터링
avg_img = average_filter(img, 5)
blur_img = cv2.blur(img, (5, 5), anchor=(-1, -1), borderType=cv2.BORDER_REFLECT)
box_img = cv2.boxFilter(img, ddepth=-1, ksize=(5, 5))

print(avg_img)

cv2.imshow("image", img)
cv2.imshow("avg_img", avg_img)
cv2.imshow("blur_img", blur_img)
cv2.imshow("box_img", box_img)
cv2.waitKey(0)