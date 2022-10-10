for i in [10, 20, 30]:
    print(i, end=",")

print()  # 출력 행을 다음 행으로 넘기기
for i in (10, 20, 30):
    print(i, end=",")

print()  # 출력 행을 다음 행으로 넘기기
for i in 'abc':
    print(i, end=',')

print()  # 출력 행을 다음 행으로 넘기기
for i in range(0, 3):
    print(i, end=',')

print()  # 출력 행을 다음 행으로 넘기기
for i in range(3): # range의 앞에 0은 생략 가능
    print(i, end=',')

print()  # 출력 행을 다음 행으로 넘기기
a = ['a', 'b', 'c']
# enumerate는 a의 원소에다가 숫자로 라벨링을 붙여줌
for k, v in enumerate(a):
    print(k, ":", v)

print()  # 출력 행을 다음 행으로 넘기기
a = [1, 2, 3]
b = [10, 20, 30]
# zip은 두 리스트를 동시에 i와 j로 가져오는 역할
for i, j in zip(a, b):
    print(i, j)