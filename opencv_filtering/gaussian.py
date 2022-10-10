import numpy as np, cv2

def getGaussianMask(ksize, sigmaX, sigmaY):
    sigma = 0.3 * ((np.array(ksize) - 1.0) * 0.5 - 1.0) + 0.8  # 표준 편차
    # 표준편차가 양수가 아니라면, ksize에 의해 계산 (OpenCV와 동일 계산)
    if sigmaX <= 0: sigmaX = sigma[0]
    if sigmaY <= 0: sigmaY = sigma[1]

    u = np.array(ksize)//2  # 평균 0을 중심으로 범위를 갖도록 커널 크기의 절반
    x = np.arange(-u[0], u[0]+1, 1)  # x방향 범위 (1간격)
    y = np.arange(-u[1], u[1]+1, 1)  # y방향 범위 (1간격)
    x, y = np.meshgrid(x, y) # 정방행렬 생성

    ratio = 1 / (sigmaX*sigmaY * 2 * np.pi)
    v1 = x ** 2 / (2 * sigmaX ** 2)
    v2 = y ** 2 / (2 * sigmaY ** 2)
    mask = ratio * np.exp(-(v1+v2))  # 최종 2차원 정규분포 수식
    return mask / np.sum(mask) # 원소 전체의 합을 1로 유지하기 위해 정규화함

img = cv2.imread("mountain.jpg", cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상 읽기 에러")

ksize = (5, 17)   # 크기는 가로x세로로 표현
gaussian_2d = getGaussianMask(ksize, 0, 0) # 직접 가우시안 마스크 생성
gaussian_1dX = cv2.getGaussianKernel(ksize[0], 0, cv2.CV_32F)   # 가로 방향 마스크
gaussian_1dY = cv2.getGaussianKernel(ksize[1], 0, cv2.CV_32F)   # 세로 방향 마스크

gauss_img1 = cv2.filter2D(img, -1, gaussian_2d) # 직접 가우시안 마스크로 필터 적용
gauss_img2 = cv2.GaussianBlur(img, ksize, 0)  # OpenCV 방법 1
gauss_img3 = cv2.sepFilter2D(img, -1, gaussian_1dX, gaussian_1dY) # OpenCV 방법 2

cv2.imshow('origin', img)
cv2.imshow('direct', gauss_img1)
cv2.imshow('OpenCV blur', gauss_img2)
cv2.imshow('OpenCV sepFilter2D', gauss_img3)
cv2.waitKey(0)