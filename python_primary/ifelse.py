# 홀수 짝수 판별하기
# 홀수: 2로 나눠 떨어지지 않으면(=나머지가 1이면)
# 짝수: 2로 나눠 떨어지면(=나머지가 0이면)
x = int(input('정수 입력: '))

if x % 2 == 1:
    print("홀수입니다.")
else:
    print("짝수입니다.")

# 이름이 guest이고, password가 0000이면 로그인
name = input('ID: ')  # id는 문자열로 받아야 함
password = input('PASSWORD: ') # password도 문자열로 받아야 함

if name == 'guest' and password == '0000':
    print('로그인 되었습니다.')
else:
    print('아이디와 패스워드를 확인하세요.')

# 1월, 3월, 5월, 7월, 8월, 10월, 12월은 31일까지 있고
# 2월은 28일까지 있으며 (윤년제외)
# 나머지는 30일까지 있다.
month = int(input('월 입력: '))

# 아래 문장을 이렇게도 쓸 수 있음
# month == 1 or month == 3 or month == 5 or \
#  month == 7 or month == 8 or month == 10 or month == 12
if month in [1, 3, 5, 7, 8, 10, 12]:
    print('31일')
elif month == 2:
    print('28일')
else:
    print('30일')

# 윤년은 4년마다 돌아오고, 그중 100년마다는 아님
# 그러나 400년마다는 윤년임
year = 2020

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('윤년')
else:
    print('평년')

# 위 if ~ else를 아래와 같이 구성해도 자연스러움
if (year % 4 == 0 and year % 100 != 0):
    print('윤년')
elif year % 400 == 0:
    print('윤년')
else:
    print('평년')