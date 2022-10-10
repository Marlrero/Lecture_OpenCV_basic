print(print) # print 함수에서, print 함수의 이름을 출력하라.
print(input)
print(int)
print(float)

a = [3.5, 1, 4, -5, 2]
# map(함수이름, 대상): 대상의 원소들을 함수를 써서 매핑시킨다.
#   -> 아래는 리스트 a의 원소를 실수(float)로 변환하라는 의미
for i in map(float, a):
    print('mappping:', i)

print('divmod:', divmod(4, 3))  # 몫과 나머지
print('max, min:', max(a), min(a)) # 리스트 a의 최댓값과 최솟값
print('type:', type(a))   # a의 타입은?
print('abs:', abs(-10))  # 절댓값
print('sum:', sum(a))   # a의 총합
print('len:', len(a))   # 리스트 a의 길이(원소의 총 개수)
print('sorted:', sorted(a))  # 리스트 a를 정렬
