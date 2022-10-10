import cv2
import numpy as np

a = np.random.randint(0, 100, 15).reshape(3, 5)
 # 0 ~ 99까지 난수를 15개 생성하고 이를 3x5 행렬로 변경

# 행 방향으로 오름차순 정렬
s1 = cv2.sort(a, cv2.SORT_EVERY_ROW)
s1_idx = cv2.sortIdx(a, cv2.SORT_EVERY_ROW)
# 열 방향으로 오름차순 정렬
s2 = cv2.sort(a, cv2.SORT_EVERY_COLUMN)
s2_idx = cv2.sortIdx(a, cv2.SORT_EVERY_COLUMN)
# 행 방향으로 내림차순 정렬 (옵션 부분 주목)
s3 = cv2.sort(a, cv2.SORT_EVERY_ROW + cv2.SORT_DESCENDING)

print('a:\n', a)
print('s1:\n', s1)
print('s1_idx:\n', s1_idx)
print('s2:\n', s2)
print('s2_idx:\n', s2_idx)
print('s3:\n', s3)
print()

# numpy로도 정렬 가능
s1 = np.sort(a, axis=1) # axis=1이면 행방향 정렬(기본 오름차순)
s2 = np.sort(a, axis=0) # axis=0이면 열방향 정렬(기본 오름차순)
s3 = np.sort(a, axis=1)[:, ::-1] # 행방향 정렬인데, 이를 거꾸로(내림차순)

print('a:\n', a)
print('s1:\n', s1)
print('s2:\n', s2)
print('s3:\n', s3)
print()

# numpy로도 정렬과 위치 알기 가능(sortIdx)
s1 = np.argsort(a, axis=0) # axis=0이면 열빙향 정렬
s2 = cv2.sortIdx(a, cv2.SORT_EVERY_COLUMN)
print('a:\n', a)
print('s1:\n', s1)
print('s2:\n', s2)

#print()
#print('a:\n', a)
#print('열 뽑기:\n', s2[:, [0]]) # 0번째 열만 뽑기 (정렬 인덱스)
#print('sort:\n', a[s2[:, [0]].astype('int')]) # 정렬 인덱스를 int로 바꿔서 a[]안에 넣으면?