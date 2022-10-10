import numpy as np

a = np.zeros((3, 4), np.int32) # 원소가 모두 0인 행렬, 3x4, 32bit integer
b = np.ones((3, 1), np.uint8) # 원소가 모두 1인 행렬, 3x1, unsigned 8bit integer
c = np.empty((1, 4), np.float64) # 원소의 값이 없는 행렬, 1x4, 64bit float
d = np.full(3, 15, np.float32) # 원소의 값이 15인 행렬, 1차원 5개, 32bit float

print(a)
print(b)
print(c) # 이 값이 [[0 0 0 0]]아닌 이상한 값이 나올 수도 있음!
         # 이는 실수표기법에 의함. 5.e-324 -> 5.0 * 10^(-324)
         # 0.24 -> 2.4 * 10^(-2) -> 2.4e-2
print(d)

print()
print(type(a), a.shape, type(a[0]), type(a[0][0]))
print(type(b), b.shape, type(b[0]), type(b[0][0]))
print(type(c), c.shape, type(c[0]), type(c[0][0]))
print(type(d), d.shape, type(d[0]))

# print(np.ndim(a)) 차원 확인