import cv2
import numpy as np

img = np.full((400, 500, 3), 255, np.uint8) # 400x500의 흰색(255) 영상 생성
poly_coord = np.array([
    (250, 30), (400, 80),
    (350, 240), (140, 180)
], np.float32)
cv2.polylines(img, [np.int32(poly_coord)], True, (0, 255, 0), 2)

# 1 radian = 1 * (180 / np.pi) = 57.2958... degree
# n radian * (180 / np.pi) -> degree
# n degree * (np.pi / 180) -> radian
rad = 20 * (np.pi / 180)  # 회전할 라디안 각도 (20도)
rotation_mat = np.array([
    [np.cos(rad), -np.sin(rad)],
    [np.sin(rad),  np.cos(rad)]
], np.float32)  # 회전 변환 행렬

# 회전 변환 공식
poly_rotate_coord = cv2.gemm(poly_coord, rotation_mat, 1.0, None, 1.0, flags=cv2.GEMM_2_T)
cv2.polylines(img, [np.int32(poly_rotate_coord)], True, (255, 0, 0), 3)

for i, (p1, p2) in enumerate(zip(poly_coord, poly_rotate_coord)):
    print(f'poly_coord[{i}] = {p1}, poly_rotate_coord[{i}] = {p2}')

cv2.imshow('rotate', img)
cv2.waitKey(0)

