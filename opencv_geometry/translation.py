import cv2
import numpy as np

def contain(p, shape): # 좌표(y,x)가 범위 안에 있는지 검사
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype) # 출력 영상 생성 (평행 이동할 화소가 없다면, 0일 것임)
    for i in range(img.shape[0]):  # 출력 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i), pt)  # 좌표는 가로x세로 순서 (평행이동 수행)
            if contain((y, x), img.shape): # 해당 이미지가 포함되면
                dst[i, j] = img[y, x] # 그 때 추가함 (포함되지 않으면 이는 제거됨)
    return dst

if __name__ == '__main__':
    image = cv2.imread('baby.jpg', cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("영상 읽기 에러")

    dst1 = translate(image, (30, 80))  # x = 30, y = 80으로 평행이동
    dst2 = translate(image, (-70, -50))

    cv2.imshow("image", image)
    cv2.imshow("dst1: trans to (80, 30)", dst1)
    cv2.imshow("dst2: trans to (-50, -70)", dst2)
    cv2.waitKey(0)
