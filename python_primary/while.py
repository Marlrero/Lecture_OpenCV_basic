# 1부터 10까지 더하는 예제
i = 1
sum = 0  # 더한 결과를 저장하려면 0으로 맞춰야 함
while i <= 10:
    sum += i   # sum = sum + i와 같음
    i += 1     # i = i + 1과 같음. i를 하나씩 증가.

print('합계:', sum)

# 1부터 10까지 더하는 예제 (break)
i = 1
sum = 0
while True:  # 조건에 True가 들어가면 무한 반복
    if i > 10:  # i가 10보다 크면
        break   # 반복문을 빠져 나가라

    sum += i   # sum = sum + i와 같음
    i += 1     # i = i + 1과 같음. i를 하나씩 증가.

print('합계:', sum)

# 3의 배수만 출력하고, 단, 100 내에서
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        print(i, end=",") # print함수의 끝을 다음줄로 넘기지 말고 ','를 넣어라.

    i += 1