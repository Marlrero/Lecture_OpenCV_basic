import cv2
import numpy as np
from translation import contain # 저번 예제와 마찬가지
from bilinear import bilinear_value

def affine_transform(img, mat):
    rows, cols = img.shape[:2]
    inv_mat = cv2.invertAffineTransform(mat)  # 어파인 변환의 역행렬(역방향)
    ## 리스트 생성 방식
    pts = [np.dot(inv_mat, (j, i, 1)) for i in range(rows) for j in range(cols)]
    #dst = [bilinear_value(img, p) if contain(p, size) else 0 for p in pts]
    dst = [bilinear_value(img, p) if contain(p, img.shape[::-1]) else 0 for p in pts]
    dst = np.reshape(dst, (rows, cols)).astype('uint8')

    ## 반복문 방식
    # dst = np.zeros(img.shape, img.dtype)  # 목적 영상 생성
    # for i in range(rows):  # 목적 영상 순회- 역방향 사상
    #     for j in range(cols):
    #         pt = np.dot(inv_mat, (j, i, 1))                # 행렬 내적 계산
    #         if contain(pt, size):  
    #            dst[i, j] = bilinear_value(img, pt)     # 화소 양선형 보간

    return dst

if __name__ == '__main__':
    img = cv2.imread('baby.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None: raise Exception("영상 읽기 에러")

    center = (200, 200)      # 회전 변환 기준 좌표
    angle, scale = 30,  1    # 회전 각도, 크기 지정 - 크기 변경은 안 함
    size = img.shape[::-1] # 영상 크기는 행렬 행태의 역순

    pt1 = np.array([(254, 120), (240, 306), (413, 198)], np.float32) # 아기 머리, 엉덩이, 인형 코
    pt2 = np.array([(120, 20), (10, 180), (280, 260)], np.float32)  # 이를 어디로 보낼지 결정하는 좌표
    aff_mat = cv2.getAffineTransform(pt1, pt2)  # 3개 좌표 쌍으로 어파인 행렬 생성
    rot_mat = cv2.getRotationMatrix2D(center, angle, scale) # 회전 변환을 위한 어파인 행렬

    dst1 = affine_transform(img, aff_mat)   # 어파인 변환 수행
    dst2 = affine_transform(img, rot_mat)   # 회전 변환 수행
    dst3 = cv2.warpAffine(img, aff_mat, size, cv2.INTER_LINEAR)
    dst4 = cv2.warpAffine(img, rot_mat, size, cv2.INTER_LINEAR)

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # 컬러 영상으로 변환해서 보여줌
    dst1 = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGR)
    dst3 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR)

    for i in range(len(pt1)):
        cv2.circle(img, tuple(pt1[i].astype(int)), 3, (0, 0, 255), 2)
        cv2.circle(dst1 , tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)
        cv2.circle(dst3 , tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)

    cv2.imshow("image", img)
    cv2.imshow("dst1_affine", dst1)
    cv2.imshow("dst2_affine_rotate", dst2)
    cv2.imshow("dst3_OpenCV_affine", dst3)
    cv2.imshow("dst4_OpenCV_affine_rotate", dst4)
    cv2.waitKey(0)