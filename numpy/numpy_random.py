import numpy as np

# 시드를 설정하지 않으면 다른 값이 나옴 (일정하게 나오기 위함)
np.random.seed(42)  # 난수 시드값으로 많이 사용함

a = np.random.rand(3, 2) # 3행 2열의 난수 배열
print(a, a.shape)
a = np.random.rand(5)  # 1차원 원소 5개 난수 배열
print(a, a.shape)

# 정규분포: 평균이 0이고 표준편차가 1임
a = np.random.randn(3, 2) # 3행 2열의 정규분포 난수 행렬
print(a, a.shape)

a = np.random.randint(1, 6, 5) # 1~6 사이의 난수로 1차원 원소 5개 배열
print(a, a.shape)