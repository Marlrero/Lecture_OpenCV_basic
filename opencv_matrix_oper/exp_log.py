import cv2
import numpy as np

a = np.array([1, 2, 3], np.float32) # 1차원 리스트로 1차원 행렬 생성
b = np.array([
    [1],
    [2],
    [3]
], np.float32) # 2차원 리스트(3x1)로 2차원 행렬 생성(-> 열벡터)
c = np.array([ [1, 2, 3] ], np.float32)
  # 2차원 리스트(1x3)로 2차원 행렬 생성(-> 행벡터)

a_exp, a_log = cv2.exp(a), cv2.log(a)
b_exp, b_log = cv2.exp(b), cv2.log(b)
c_exp, c_log = cv2.exp(c), cv2.log(c)

a_sqrt, a_pow = cv2.sqrt(a), cv2.pow(a, 2)
b_sqrt, b_pow = cv2.sqrt(b), cv2.pow(b, 2)
c_sqrt, c_pow = cv2.sqrt(c), cv2.pow(c, 2)

print(f'a: shape({a.shape}\n{a}')
print(f'b: shape({b.shape}\n{b}')
print(f'c: shape({c.shape}\n{c}')
print()

print(f'exp(a): shape({a_exp.shape}\n{a_exp}')
print(f'exp(b): shape({b_exp.shape}\n{b_exp}')
print(f'exp(c): shape({c_exp.shape}\n{c_exp}')
print()

print(f'log(a): shape({a_log.shape}\n{a_log}')
print(f'log(b): shape({b_log.shape}\n{b_log}')
print(f'log(c): shape({c_log.shape}\n{c_log}')
print()

print(f'sqrt(a): shape({a_sqrt.shape}\n{a_sqrt}')
print(f'sqrt(b): shape({b_sqrt.shape}\n{b_sqrt}')
print(f'sqrt(c): shape({c_sqrt.shape}\n{c_sqrt}')
print()

print(f'pow(a): shape({a_pow.shape}\n{a_pow}')
print(f'pow(b): shape({b_pow.shape}\n{b_pow}')
print(f'pow(c): shape({c_pow.shape}\n{c_pow}')
print()

# 열벡터를 한 행에 출력
print('b.T:\n', b_pow.T) # 전치하여 1행 3열로 변경
print('ravel:\n', np.ravel(b_pow))
print('flatten:\n', b_pow.flatten())