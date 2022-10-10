import numpy as np
import matplotlib.pyplot as plt

def getPDF(x, mu, sigma): # 입력, 평균, 표준편차
    return (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(-(x-mu)**2 / (2 * sigma**2))

np.random.seed(41) # 난수 시드 값

x = np.linspace(-8, 8, 1000) # -8부터 8까지 1000개의 일정한 숫자
y1 = getPDF(x, 0.0, 1.0) # 평균이 0이고 표준편차가 1인
                     # 표준 정규분포 (Standard Probability Density Function)
y2 = getPDF(x, 0.0, 5.0)
y3 = getPDF(x, 0.0, 0.5)

plt.figure(figsize=(12, 8)) # 그래프 사이즈(인치)
plt.title('Standard Normal Distribution') # 그래프 제목
plt.xlabel('x') # x축 라벨
plt.ylabel('f(x)') # y축 라벨
plt.grid() # 격자 생성

plt.plot(x, y1, alpha=0.7, label="Probability Density Function of N(0, 1)") # 표준
plt.plot(x, y2, alpha=0.7, label="Probability Density Function of N(0, 5)")
plt.plot(x, y3, alpha=0.7, label="Probability Density Function of N(0, 0.5)")

plt.legend(loc='upper left') # 범례를 왼쪽 상단에 넣기
plt.show()