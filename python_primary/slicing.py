x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(x)   # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(x[0:2])   # [10, 20]  -> 2번째 원소인 30은 가져오지 않음
print(x[:2])    # [10, 20]  -> 시작에서 0 생략 가능
print(x[6:10])  # [70, 80, 90, 100] -> 6번째부터 10-1=9번째 원소까지 가져옴
print(x[6:])    # [70, 80, 90, 100] -> 끝을 생략하면 원소 끝 까지를 의미
print(x[6:-1])  # [70, 80, 90] -> 끝에서 -1을 쓰면, 마지막 원소를 의미
print(x[2::2])  # [30, 50, 70, 90] -> 증감에서 2는 오른쪽으로 2칸 이동
print(x[::-1])  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] -> 역순 출력
print(x[1::-1]) # [20, 10] -> 첫 두 개 원소만 역순으로 출력