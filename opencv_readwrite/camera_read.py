from utils import add_string_frame
import cv2

camera = cv2.VideoCapture(0) # 카메라(웹캠) 연결되어 있어야 함
if not camera.isOpened():  # camera.isOpened() == False
    raise Exception("카메라 연결되어 있지 않음")

# 카메라 속성ID로 속성값 보기
print(f"너비: {camera.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"높이: {camera.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f'fps: {camera.get(cv2.CAP_PROP_FPS)}')
print(f"노출: {camera.get(cv2.CAP_PROP_EXPOSURE)}")
print(f"밝기: {camera.get(cv2.CAP_PROP_BRIGHTNESS)}")

while True:  # 카메라 이미지를 받으려면 계속 반복해야 함
    ret, frame = camera.read()
    if not ret:  # 카메라에서 더이상 프레임이 없다면(ret에서 False가 넘어옴)
        break  # 종료
    if cv2.waitKey(30) >= 0: # 스페이스바를 누르면
        break  # 종료
    
    exposure = camera.get(cv2.CAP_PROP_EXPOSURE)
    add_string_frame(frame, (10, 40), "Exposure: ", exposure)
    cv2.imshow("Camera", frame)  # 창에 현재 화면 출력

camera.release()  # 카메라 연결 종료

