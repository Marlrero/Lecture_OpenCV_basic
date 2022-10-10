import cv2

# 딕셔너리는 key와 value으로 구성됨
key_print = {
    ord('a'): 'a키',  # ord 함수는 ASCII code로 변환함
    ord('A'): 'A키',
    int('0x250000', 16): '왼쪽 화살표키'  # 16진수 0x250000을 int값으로 변경
}

cv2.namedWindow('Key Event')

while True:  # 무한반복
    key_code = cv2.waitKeyEx(100) # 100ms 키보드 입력대기
    if key_code == 27:  # ESC를 누르면
        break # 이 무한반복을 빠져나감
    
    if key_code in key_print.keys(): # 키 코드가 key_print 안에 키로 존재한다면
        print(key_print[key_code])
    else:
        print('처리할 수 없음!')

cv2.destroyAllWindows()