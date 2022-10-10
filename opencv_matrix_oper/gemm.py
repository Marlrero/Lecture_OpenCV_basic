import cv2
import numpy as np

a = np.array([1, 2, 3, 1, 2, 3], np.float32).reshape(2, 3)
b = np.array([1, 2, 3, 4, 5, 6], np.float32).reshape(2, 3)
c = np.array([1, 2, 1, 2, 1, 2], np.float32).reshape(3, 2)
alpha, beta = 1.0, 1.0

r1 = cv2.gemm(a, b, alpha, None, beta, flags=cv2.GEMM_1_T)
 # (2, 3)T * (2, 3) -> (3, 2) * (2, 3) = (3, 3)
r2 = cv2.gemm(a, b, alpha, None, beta, flags=cv2.GEMM_2_T)
 # (2, 3) * (2, 3)T -> (2, 3) * (3, 2) = (2, 2)
r3 = cv2.gemm(a, c, alpha, None, beta)
 # (2, 3) * (3, 2) = (2, 2)

print('r1:\n', r1)
print('r2:\n', r2)
print('r3:\n', r3)

# numpy에도 내적이 존재
print()
print('r1:\n', a.T.dot(b))  # dot() 함수로 내적 가능 (T는 전치)
print('r2:\n', a.dot(b.T))
print('r3:\n', a.dot(c))
print('r3:\n', a @ c) # '@' 연산자로도 내적 가능