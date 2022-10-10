import cv2
import numpy as np

from bilinear import bilinear_value
  # 양선형보간 (bilinear.py에서 if __name__ == '__main__')
from translation import contain
  # 사각형으로 범위 확인 함수 (translation.py에서 if __name__ == '__main__')

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype) # 출력 영상 생성
    radian = (degree/180) * np.pi   # 회전 각도 - 라디언
    sin, cos = np.sin(radian), np.cos(radian)  # 사인, 코사인 값 미리 계산

    for i in range(img.shape[0]):  # 출력 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x =  j * cos + i * sin  # 회전 변환 수식
            if contain((y, x), img.shape):  # 입력 영상의 범위이면 화소 이동
                dst[i, j] = bilinear_value(img, [x, y])  # 화소값 양선형 보간
    return dst

def rotate_pt(img, degree, pt):  # 원점이 아닌 pt 기준으로 회전
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)  # 중심좌표 평행이동
            y = -jj * sin + ii * cos
            x =  jj * cos + ii * sin  # 회전 변환 수식
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):  # 입력 영상의 범위이면 화소 이동
                dst[i, j] = bilinear_value(img, [x, y])  # 화소값 양선형 보간
    return dst

image = cv2.imread('baby.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 읽기 에러")

center = np.divmod(image.shape[::-1], 2)[0] # 이미지의 중심 좌표
dst1 = rotate(image, 20)   # 원점 기준 회전 변환
dst2 = rotate_pt(image, 20, center) # 영상 중심 기준 회전 변환

cv2.imshow("image", image)
cv2.imshow("dst1-rotated on org", dst1)
cv2.imshow("dst2-rotated on center", dst2)
cv2.waitKey(0)