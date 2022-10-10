import cv2
import numpy as np

x = np.array([1, 2, 3, 5, 10], np.float32) # 리스트로 5x1행렬(열벡터) 생성
y = np.array([2, 2, 7, 3, 8]).astype('float32') # 리스트로 5x1행렬(열벡터) 생성

mag = cv2.magnitude(x, y) # 크기
ang = cv2.phase(x, y)     # 각도(방향)
polar_mag, polar_ang = cv2.cartToPolar(x, y) # 극 좌표 변환
x2, y2 = cv2.polarToCart(polar_mag, polar_ang) # 직교 좌표 변환

print(f'x: shape({x.shape}\n{x}')
print(f'y: shape({y.shape}\n{y}')
print()

print(f'magnitude(x, y): shape({mag.shape}\n{mag}')
print(f'phase(x, y): shape({ang.shape}\n{ang}')
print()

print(f'cartToPolar(x, y) - mag: shape({polar_mag.shape}\n{polar_mag}')
print(f'cartToPolar(x, y) - ang: shape({polar_ang.shape}\n{polar_ang}')
print()

print(f'polarToCart(mag, ang) - x: shape({x2.shape}\n{x2}')
print(f'polarToCart(mag, ang) - y: shape({y2.shape}\n{y2}')
print()