import cv2
import numpy as np

# 3x6의 10과 50으로 가득 찬 배열 생성
a = np.full((3, 6), 10, np.uint8)
b = np.full((3, 6), 10, np.uint8)
# 배열 a의 shape(3x6)와 같은 원소가 모두 0인 배열 생성
masking = np.zeros(a.shape, np.uint8)
print('masking_prev:\n', masking)
masking[:, 3:] = 1 # 모든 행에서 3번째 열부터 끝까지 1로 바꿔라
print('masking_next:\n', masking)
print()

# 일반 행렬 덧셈과 마스킹 적용 덧셈
print('add:\n', cv2.add(a, b))
print('mask add:\n', cv2.add(a, b, mask=masking))
print()

print('divide uint8:\n', cv2.divide(a, b)) # 정수형 나눗셈 수행
a = a.astype(np.float32) # 배열 a의 타입을 uint8에서 float32로 변경
b = np.float32(b) # 배열 b의 타입을 unit8에서 float32로 변경
print('divide float32:\n', cv2.divide(a, b)) # 실수형 나눗셈 수행
print()