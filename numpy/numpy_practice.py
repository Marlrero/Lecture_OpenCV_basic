import numpy as np  # numpy 라이브러리 불러오기(별명 np)

a = [1, 2, 3]
b = [4, 5, 6]  # 리스트
x = np.array(a) # 리스트로 ndarray로
y = np.array(b)

print(x, type(x), type(x[0]))
print(y, type(y), type(y[0]))

z = x + y # np.add(x, y) -> 행렬 덧셈
print(z, type(z))
z = x - y # np.subtract(x, y) -> 행렬 뺄셈
print(z, type(z))
z = x * y # np.multiply(x, y) -> 행렬 원소 곱(실제 행렬 곱 아님 주의)
print(z, type(z))
z = x / y # np.divide(x, y) -> 행렬 나눗셈
print(z, type(z))

z = x * 2.0 # 스칼라 곱
print(z, type(z), type(z[0]))  # 실수를 곱했기 때문에 float64
z = x + 2 # 스칼라 합
print(z, type(z), type(z[0]))
