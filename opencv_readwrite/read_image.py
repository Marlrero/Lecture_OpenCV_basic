from utils import print_matrix_info
import cv2

title1, title2 = 'gray_image', 'color_image'
# 경로가 이 소스파일과 같은 폴더안에 위치해야 함
gray_image = cv2.imread("apple.jpg", cv2.IMREAD_GRAYSCALE)
color_image = cv2.imread("apple.jpg", cv2.IMREAD_COLOR)

# 영상파일이 잘 읽혔는지 검사
if gray_image is None or color_image is None:
    raise Exception('영상파일 읽기 에러') # 예외(에러) 발생

print("행렬 좌표(100, 100)에 대한 화소 값: ")
print(f'{title1}, {gray_image[100, 100]}')
print(f'{title2}, {color_image[100, 100]}')

print_matrix_info(title1, gray_image)
print_matrix_info(title2, color_image)

cv2.imshow(title1, gray_image)
cv2.imshow(title2, color_image)
cv2.waitKey(0)