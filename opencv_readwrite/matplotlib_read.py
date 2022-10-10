import cv2
import matplotlib.pyplot as plt

img = cv2.imread('apple.jpg', cv2.IMREAD_COLOR)
if img is None:
    raise Exception('영상파일 열기 실패')

print('image shape: ', img.shape) # 세로, 가로, 채널
rows, cols = img.shape[:2] # 0 ~ 1(세로, 가로)까지 자르라는 의미

# matplotlib는 색 공간이 RGB 형태로 줘야 하므로,
# 기존 OpenCV의 BGR 형태를 변형해야 함
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fig = plt.figure(num=1, figsize=(3, 4)) # Figure 크기 지정
plt.imshow(img)
plt.title('Figure1 - BGR image') # 타이틀 지정
plt.axis('off')  # 축 안보이게 하기
plt.tight_layout() # 여백 없게 함


fig = plt.figure(figsize=(6, 4)) # Figure 크기 지정
plt.suptitle('Figure2 - Convert image') # 전체 타이틀 지정

plt.subplot(1, 2, 1) # 1행 2열의 index가 1인 서브 플롯
plt.imshow(rgb_img)
plt.axis([0, cols, rows, 0]) # 축 범위 지정
plt.title('RGB color') # 한 플롯 타이틀 지정

plt.subplot(1, 2, 2) # 1행 2열의 index가 2인 서브 플롯
plt.imshow(gray_img, cmap='gray') # 컬러맵을 그레이스케일로
plt.title('Gray color') # 한 플롯 타이틀 지정

plt.show()