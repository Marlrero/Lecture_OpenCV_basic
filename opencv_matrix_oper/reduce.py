import cv2
import numpy as np

# rand(3, 5): 3x5 난수(0부터 1사이의 값) 행렬 생성
# 그 값에 100을 곱하면 0 ~ 100미만의 난수가 생성됨
a = np.random.rand(3, 5) * 100

r_sum = cv2.reduce(a, dim=0, rtype=cv2.REDUCE_SUM) # 행방향 합
r_avg = cv2.reduce(a, dim=1, rtype=cv2.REDUCE_AVG) # 열방향 곱
r_max = cv2.reduce(a, dim=0, rtype=cv2.REDUCE_MAX) # 행방향 최댓값
r_min = cv2.reduce(a, dim=1, rtype=cv2.REDUCE_MIN) # 열방향 최솟값

print("a:\n", a)
print("sum:\n", r_sum)
print("avg:\n", r_avg)
print("max:\n", r_max)
print("min:\n", r_min)