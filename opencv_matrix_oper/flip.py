import cv2

img = cv2.imread('pyramid.jpg', cv2.IMREAD_COLOR)
if img is None:
    raise Exception('영상파일 열기 실패')

x_axis = cv2.flip(img, 0)
y_axis = cv2.flip(img, 1)
xy_axis = cv2.flip(img, -1)

titles = ['origin', 'x_axis', 'y_axis', 'xy_axis']
imgs = [img, x_axis, y_axis, xy_axis]
for a in range(len(titles)):
    cv2.imshow(titles[a], imgs[a])

import numpy as np
x = np.arange(10).reshape(2, 5)
print(x)
print('x_axis')
print(x[::-1])
print(np.flip(x, axis=0))
print('y_axis')
print(x[:, ::-1])
print(np.flip(x, axis=1))
print('xy_axis')
print(x[::-1, ::-1])
print(np.flip(x))

cv2.waitKey(0)
