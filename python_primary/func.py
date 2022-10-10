def plus(a, b):   # 함수 정의
    print('plus 함수 실행 중...')
    return a + b

c = plus(1, 2)    # 함수 호출
print(c)
print()
###################################################
# 파이썬에서 값이 바뀌지 않아야할 상수는 대문자로 표시 관례
PI = 3.141592

# radius도 변수! 입력을 받는 변수. 단, 함수 안에서만 사용 가능.
def get_circumference(radius):
    return 2 * PI * radius

def get_area(radius):
    return PI * radius * radius

# 주의: 여기서 radius는 함수의 입력인 radius와는 다른 변수
radius = float(input("원 반지름 입력: "))
print('원 둘레:', get_circumference(radius))
print('원 넓이:', get_area(radius))
print()
###################################################
def print_privacy(p):  # p는 개인정보가 담긴 딕셔너리 입력
    # 딕셔너리는 키로 접근해야 하므로, 없는 키면 에러가 발생함
    if "name" in p:  # 딕셔너리 p에 키 name이 있는가?
        print("Name:", p['name'])        

    if "age" in p:   # 딕셔너리 p에 키 age가 있는가?
        print("Age:", p['age'])
    
    # 이렇게 함수는 출력(return)이 없을 수 있음

a = { "name": "wooju", "age": 23 }
b = { "age": 50 }

print_privacy(a)
print_privacy(b)  # 이것이 정상인가? 이름이 없이 나이만 출력되는 것이?
print()
###################################################
# 위 함수의 개선 버전
def print_privacy(p):
    if "name" in p: 
        print("Name:", p['name'])
    else:
        print("잘못된 정보입니다.")
        # 이름이 없으므로 나이를 출력할 필요가 없으니,
        # 여기서 return하면 함수는 아무것도 리턴하지 않고 종료
        return

    if "age" in p: 
        print("Age:", p['age'])


a = {"name": "wooju", "age": 23}
b = {"age": 50}

print_privacy(a)
print_privacy(b)

