'''
   circle.py
   파이썬에서 원의 길이와 넓이를 출력하는 프로그램

   제작일: 2022. 1. 20
'''

PI = 3.14   # 파이썬에서 상수에 이름을 달 때는 이름을 대문자로 쓰는 것이 관례임
radius = int(input('정수 반지름 입력: '))   # x 입력

print("원 길이:", 2 * PI * radius)    # 2*pi*r
print("원 넓이:", PI * radius * radius)  # pi * (radius**2)로 써도 동일함