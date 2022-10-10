import cv2
import numpy as np

def scaling_nearest(img, size):  # 크기 변경(이웃화소)
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1) # 출력 영상의 세로 범위만큼 좌표 생성 (1씩)
    j = np.arange(0, size[0], 1) # 출력 영상의 가로 범위만큼 좌표 생성 (1씩)
    i, j = np.meshgrid(i, j) # 출력 영상의 좌표를 가지고 정방행렬 생성
    y, x = np.int32(i / ratioY), np.int32(j / ratioX) # 크기 변경 수식 (역방향 사상)
    dst[i, j] = img[y, x] # 이를 행렬에 그대로 복사
    return dst

def bilinear_value(img, pt): # 단일 화소에 대한 양선형 보간
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x -1
    if y >= img.shape[0]-1: y = y - 1

    P1, P4, P2, P3 = np.float32(img[y:y+2,x:x+2].flatten())
    # 4개의 화소 가져옴 – 화소 직접 접근 방법
    #  P1 = float(img[y, x] )         # 상단 왼쪽 화소
    #  P4 = float(img[y + 0, x + 1])  # 상단 오른쪽 화소
    #  P2 = float(img[y + 1, x + 0])  # 하단 왼쪽 화소
    #  P3 = float(img[y + 1, x + 1])  # 하단 오른쪽 화소

    alpha, beta = pt[1] - y,  pt[0] - x   # 거리 비율
    M1 = P1 + alpha * (P2 - P1)  # 1차 보간
    M2 = P4 + alpha * (P3 - P4)
    P  = M1 + beta  * (M2 - M1)  # 2차 보간
    return  np.clip(P, 0, 255)   # 화소값 saturation(0 ~ 255 사이로)후 반환

def scaling_bilinear(img, size): # 양선형 보간
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])  # 변경 크기 비율

    dst = [ [ bilinear_value(img, (j/ratioX, i/ratioY)) for j in range(size[0])]
                  for i in range(size[1])] # size[1]xsize[0] 짜리 리스트 생성
    return np.array(dst, img.dtype)

if __name__ == '__main__':
    img = cv2.imread('baby.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None: raise Exception("영상 읽기 에러")

    size = (800, 600)
    dst1 = scaling_bilinear(img, size)   # 크기 변경 - 양선형 보간
    dst2 = scaling_nearest(img, size)    # 크기 변경 - 최근접이웃 보간
    dst3 = cv2.resize(img, size, 0, 0, cv2.INTER_LINEAR)  # OpenCV 함수 적용 (양선형)
    dst4 = cv2.resize(img, size, 0, 0, cv2.INTER_NEAREST) # OpenCV 함수 적용 (최근접이웃)

    cv2.imshow("image", img)
    cv2.imshow("User_bilinear", dst1)
    cv2.imshow("User_Nearest", dst2)
    cv2.imshow("OpenCV_bilinear", dst3)
    cv2.imshow("OpenCV_Nearest", dst4)
    cv2.waitKey(0)