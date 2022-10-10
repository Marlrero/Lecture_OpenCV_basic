import cv2
import numpy as np
import matplotlib.pyplot as plt

# 25개 (x, y) 좌표 -> 이 좌표는 0 ~ 99사이 값 (훈련데이터)
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
# 25개 (x, y) 좌표가 어느 클래스에 있는지 0 ~ 1사이의 값으로 선정 (훈련데이터에 레이블, 정답)
responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# 빨간색 클래스(클래스 0)
red = trainData[responses.ravel() == 0]
plt.scatter(red[:,0], red[:,1], 80, 'r', '^') # red(x, y), 80픽셀, red, 삼각형

# 파란색 클래스(클래스 1)
blue = trainData[responses.ravel() == 1]
plt.scatter(blue[:,0], blue[:,1], 80, 'b', 's') # blue(x, y), 80픽셀, red, 사각형

# 새로운 한 점이 왔을 때
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

# knn
knn = cv2.ml.KNearest_create() # kNN 모델 만들기
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses) # 훈련 데이터, 훈련 데이터가 행/열 여부, 정답
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3) # 새로운 샘플, k값

print("result: ", results)
print("neighbours: ", neighbours)
print("distance: ", dist)

plt.show()