import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10) # x축 데이터: 0, 1, 2, ..., 9
y1 = np.arange(10) # y축 데이터
y2 = np.arange(10) ** 2 # y1 데이터의 제곱 배 값
y3 = np.random.choice(50, size=10) # 0~49까지 숫자 10개 뽑기

plt.figure(figsize=(5, 3)) # Figure 크기 지정
plt.plot(x, y1, '--b', linewidth=2) # 파선 파란색, 굵기 2
plt.plot(x, y2, 'o-g', linewidth=3) # 원마크 실선 초록색, 굵기 3
plt.plot(x, y3, '+:c', linewidth=5) # +마크 점선 시안(청록)색, 굵기 5

plt.title('Line graph')
plt.axis([0, 10, 0, 80]) # xmin, xmax, ymin, ymax
plt.tight_layout() # 여백 없음
plt.savefig(fname='graph.png', dpi=300) # graph.png로 DPI가 300 저장
plt.show()
