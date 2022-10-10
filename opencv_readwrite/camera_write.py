import cv2

camera = cv2.VideoCapture(0)  # 카메라(웹캠) 연결되어 있어야 함
if not camera.isOpened():  # camera.isOpened() == False
    raise Exception("카메라 연결되어 있지 않음")

# 카메라에서 받아온 영상을 저장하기 위한 설정 값
fps = 29.97  # 30
# delay = round(1000/fps)  # 프레임간 지연 시간
size = (640, 480)  # 프레임 가로x세로
fourcc = cv2.VideoWriter_fourcc(*'MP4V') # 코덱 설정

camera.set(cv2.CAP_PROP_FRAME_WIDTH, size[0]) # 프레임에 맞게 카메라도 설정
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

# 동영상파일 오픈
writer = cv2.VideoWriter("camera_record.mp4", fourcc, fps, size)
if not writer.isOpened():
    raise Exception("동영상파일 열기 실패")

while True:  # 카메라 이미지를 받으려면 계속 반복해야 함
    ret, frame = camera.read()
    if not ret:  # 카메라에서 더이상 프레임이 없다면(ret에서 False가 넘어옴)
        break  # 종료
    if cv2.waitKey(int(1000/fps)) >= 0:  # 딜레이 종료
        break  # 종료

    writer.write(frame) # 프레임을 동영상 파일에 쓰기
    cv2.imshow("Camera", frame)  # 창에 현재 화면 출력

writer.release()  # 동영상 파일 연결 종료
camera.release()  # 카메라 연결 종료

