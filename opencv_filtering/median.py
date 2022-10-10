import cv2
import numpy as np

def median_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2    # 마스크 절반 크기

    for i in range(center, rows - center): # 입력 영상 순회
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1  # 마스크 높이 범위
            x1, x2 = j - center, j + center + 1  # 마스크 너비 범위
            mask = image[y1:y2, x1:x2].flatten() # 마스크 영역

            sort_mask = cv2.sort(mask, cv2.SORT_EVERY_COLUMN) # 정렬 수행
            dst[i, j] = sort_mask[sort_mask.size//2]  # 출력은 중간값

    return dst

def salt_pepper_noise(image, n):
    h, w = image.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
      # 0 ~ 가로 크기만큼 n개의 난수, 0 ~ 세로 크기만큼 n개의 난수 (위치 좌표 난수)
    noise = image.copy()
    for (x,y) in zip(x,y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255
        # 0 ~ 1 사이의 실수 난수를 만들고, 이 값이 0.5보다 작으면 0, 그렇지 않으면 255
    return noise

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

noise_img = salt_pepper_noise(img, 500)
#med_img = median_filter(img, 3)   # 직접 만든 메디안 필터링
med_img1 = median_filter(noise_img, 3)   # 직접 만든 메디안 필터링
med_img2 = cv2.medianBlur(noise_img, 3)  # OpenCV 제공 함수

#print(med_img)

cv2.imshow("image", img)
cv2.imshow("noise_img", noise_img)
cv2.imshow("med_img1", med_img1)
cv2.imshow("med_img2", med_img2)
cv2.waitKey(0)