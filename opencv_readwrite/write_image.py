import cv2

# 경로가 이 소스파일과 같은 폴더안에 위치해야 함
image = cv2.imread("apple.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception('영상파일 읽기 에러')

param_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10) # 0 ~ 100(높을수록 화질 좋음)
param_png = [cv2.IMWRITE_PNG_COMPRESSION, 9] # 0 ~ 9(높을수록 압축률 좋음)

cv2.imwrite("apple_write_best.jpg", image) # JPEG_QUALITY 기본값은 95
cv2.imwrite("apple_write.jpg", image, param_jpg)
cv2.imwrite("apple_write.png", image, param_png)

cv2.waitKey(0)