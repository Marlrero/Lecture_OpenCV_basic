import cv2
import numpy as np

ch0 = np.zeros((2, 4), np.uint8) + 10
ch1 = np.ones((2, 4), np.uint8) * 20
ch2 = np.full((2, 4), 30, np.uint8)

bgr = [ch0, ch1, ch2]
merge_bgr = cv2.merge(bgr) # 단일 채널을 모아 합치기(BGR)
split_bgr = cv2.split(merge_bgr) # 모은 것을 분리(B, G, R 분리)

print('merge shape:', merge_bgr.shape)  # 2, 4, 3
print('split shape:', np.array(split_bgr).shape)  # 3, 2, 4
print('merge:\n', merge_bgr)
print('split0:\n', split_bgr[0])
print('split1:\n', split_bgr[1])
print('split2:\n', split_bgr[2])

