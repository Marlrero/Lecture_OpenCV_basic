import numpy as np

a = np.array([1, 2, 3, 4]) # 1차원 4개 원소 행렬
print(a, a.shape)

b = np.reshape(a, (2, 2))  # 2x2 행렬로 변경
print(b, b.shape)

c = a.reshape(2, -1)
# -1의 의미는, 알아서 하라는 의미
# (2, -1)이므로, 원래 행렬 a의 원소가 4개이므로 2x2로 reshape
print(c, c.shape)

d = c.reshape(-1) # c.reshape(1, -1) -> 1차원과 동일
print(d, d.shape)

e = c.flatten()
print(e, e.shape) # 위와 동일한 기능