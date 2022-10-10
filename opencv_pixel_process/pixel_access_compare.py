import cv2, time
import numpy as np

def pixel_inverse_numpy1(img):
    result = np.zeros(img.shape[:2], img.dtype)  # 이미지 가로x세로에 맞는 0(흰색) 영상 생성

    for i in range(img.shape[0]): # 가로 크기만큼 반복
        for j in range(img.shape[1]): # 세로 크기만큼 반복
            result[i, j] = 255 - img[i, j]

    return result

def pixel_inverse_numpy2(img):
    result = np.zeros(img.shape[:2], img.dtype)  # 이미지 가로x세로에 맞는 0(흰색) 영상 생성

    for i in range(img.shape[0]): # 가로 크기만큼 반복
        for j in range(img.shape[1]): # 세로 크기만큼 반복
            result.itemset((i, j), 255 - img.item(i, j))

    return result

def pixel_inverse_numpy3(img):
    result = np.zeros(img.shape[:2], img.dtype)  # 이미지 가로x세로에 맞는 0(흰색) 영상 생성
    result = 255 - img

    return result

def pixel_inverse_lut(img):
    result = np.zeros(img.shape[:2], img.dtype)  # 이미지 가로x세로에 맞는 0(흰색) 영상 생성
    lut = np.array([255 - i for i in range(256)], np.uint8)
    result = lut[img]

    return result

def pixel_inverse_opencv(img):
    result = np.zeros(img.shape[:2], img.dtype)  # 이미지 가로x세로에 맞는 0(흰색) 영상 생성
    result = cv2.subtract(255, img)

    return result

def get_time(func, msg):
    img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None: raise Exception('영상 읽기 에러')

    start = time.perf_counter() # 시작!
    result = func(img) # func 함수 실행 중
    end = time.perf_counter()  # 끝!

    elapsed = (end - start) * 1000  # ms 단위로 변경
    print(f'{msg} 수행시간: {elapsed:0.2f} ms')
    #print(f'{msg} 수행결과:\n{result}')
    cv2.imshow(msg, result)

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Origin', img)

get_time(pixel_inverse_numpy1, 'Numpy ndarray 1')
get_time(pixel_inverse_numpy2, 'Numpy ndarray 2')
get_time(pixel_inverse_numpy3, 'Numpy ndarray 3')
get_time(pixel_inverse_lut, 'Lookup Table')
get_time(pixel_inverse_opencv, 'OpenCV function')
cv2.waitKey(0)