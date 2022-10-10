from utils import add_string_frame
import cv2

# 카메라 연결
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise Exception("카메라 연결되어 있지 않음")

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 400)  # 프레임 가로 400 지정
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)  # 프레임 세로 300 지정
camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # 자동초점 정지
camera.set(cv2.CAP_PROP_BRIGHTNESS, 100)  # 프레임 밝기 100 지정

# 이벤트 처리 함수
def zoom_bar(value):  # 줌인-아웃 트랙바 이벤트 처리 함수
    global camera  # camera라는 변수는 바깥에 있음을 알림
    camera.set(cv2.CAP_PROP_ZOOM, value)  # 줌 설정

def focus_bar(value):  # 포커스 조정 트랙바 이벤트 처리 함수
    global camera
    camera.set(cv2.CAP_PROP_FOCUS, value)  # 포커스 설정

# 화면 구성
window_name = "Camera"
cv2.namedWindow(window_name)  # 타이틀이 Camera인 윈도우 생성
cv2.createTrackbar('zoom', window_name, 0, 10, zoom_bar)  # 줌인-아웃 트랙바 생성
cv2.createTrackbar('focus', window_name, 0, 40, focus_bar)  # 포커스 조정 트랙바 생성

# 화면 출력
while True:  # 카메라 이미지를 받으려면 계속 반복해야 함
    ret, frame = camera.read()
    if not ret:  # 카메라에서 더이상 프레임이 없다면(ret에서 False가 넘어옴)
        break  # 종료
    if cv2.waitKey(30) >= 0:  # 스페이스바를 누르면
        break  # 종료

    zoom = int(camera.get(cv2.CAP_PROP_ZOOM)) # 줌 값 가져오기
    focus = int(camera.get(cv2.CAP_PROP_FOCUS)) # 초점 값 가져오기
    add_string_frame(frame, (10, 240), 'Zoom: ', zoom)
    add_string_frame(frame, (10, 270), 'Focus: ', focus)
    cv2.imshow(window_name, frame)  # 창에 현재 화면 출력

camera.release()  # 카메라 연결 종료
