import cv2
from utils import add_string_frame

video = cv2.VideoCapture('sample_video.mp4')
if not video.isOpened():
    raise Exception('동영상파일 열기 실패')

fps = video.get(cv2.CAP_PROP_FPS)
print(f'총 프레임 수: {video.get(cv2.CAP_PROP_FRAME_COUNT)}')
delay = int(1000 / fps)  # 지연시간
frame_cnt = 0  # 현재 프레임 번호

while True:
    ret, frame = video.read()
    if not ret or cv2.waitKey(delay) >= 0:
        break

    blue, green, red = cv2.split(frame) # 컬러 채널 분리 (BGR)
    frame_cnt += 1 # 현재 프레임 번호 1 증가

    if 100 <= frame_cnt < 200:
        # cv2.add(a, b, c): a + b = c (배열의 원소끼리 합)
        cv2.add(blue, 100, blue)  # blue 채널 밝기 증가
    elif 200 <= frame_cnt < 300:
        cv2.add(green, 100, green) # green 채널 밝기 증가
    elif 300 <= frame_cnt < 400:
        cv2.add(red, 100, red) # red 채널 밝기 증가

    frame = cv2.merge([blue, green, red])  # 단일 채널로 합치기(합성)
    add_string_frame(frame, (20, 30), 'frame#: ', frame_cnt)
    cv2.imshow("Video File", frame)

video.release()