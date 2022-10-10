import cv2, numpy as np
import pickle, gzip, os
#from urllib.request import urlretrieve
import matplotlib.pyplot as plt

def load_mnist(filename):
    '''
    if not os.path.exists(filename):
        print("Downloading" )
        link = "http://deeplearning.net/data/mnist/mnist.pkl.gz"
        urlretrieve(link, filename)
    '''
    with gzip.open(filename, 'rb') as f:
        return pickle.load(f, encoding='latin1')

def graph_image(data, lable, title, nsample): # nsample개의 데이터를 이미지 표시
    plt.figure(num=title, figsize=(6, 9))
    rand_idx = np.random.choice(range(data.shape[0]), nsample) # 랜덤하게 고름
    for i, id in enumerate(rand_idx):
        img = data[id].reshape(28, 28) # 이미지를 28x28로 조정
        plt.subplot(6, 4, i + 1), plt.axis('off'), plt.imshow(img, cmap='gray')
        plt.title(f'{title}: {lable[id]}')
    plt.tight_layout()

train_set, valid_set, test_set = load_mnist('mnist.pkl.gz')
train_data, train_label = train_set # 데이터(이미지)와 정답
test_data, test_label = test_set # 데이터(이미지)와 정답
## MNIST 로드 데이터 크기 확인
print('train_set=', train_set[0].shape) # 50000개, 28x28 = 784
print('valid_set', valid_set[0].shape) # 10000개, 28x28 = 784
print('test_set', test_set[0].shape) # 10000개, 28x28 = 784

print('training...')
knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_label)  # k-NN 학습 수행
# 훈련 데이터, 행/열단위인지, 훈련 데이터의 정답

nsample = 10
print(f"{nsample}개 predicting...")
_, results, neighbours , dist = knn.findNearest(test_data[:nsample], k=5)   # k-NN 분류 수행
print("result: ", results)
print("neighbours: ", neighbours)
print("distance: ", dist)

accur = sum(test_label[:nsample] == results.flatten()) / len(results)    # 성능 측정

print("정확도=", accur*100, '%')
graph_image(train_data, train_label, 'label', 24)  # 훈련 데이터 그리기
graph_image(test_data[:nsample], results, 'predict', 24) # 테스트 데이터 그리기
plt.show()