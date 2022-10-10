import cv2

def onTrackbar(th):	# 트랙바 콜백 함수
    edgeImg = cv2.GaussianBlur(grayImg, (5, 5), 0)  # 가우시안 블러링
    edgeImg = cv2.Canny(edgeImg, th, th*2, 5)	# 캐니 에지 검출
    h, w = img.shape[:2]
    cv2.rectangle(edgeImg, (0, 0, w, h), 255, -1) # 흰색 사각형 그리기
    colorEdge = cv2.bitwise_and(rep_image, rep_image, mask=edgeImg)
    # 같은 행렬로 and 연산을 하면 결국 복사한다는 의미
    # mask가 edgeImg이고, edgeImg의 원소가 1이상인 위치만 복사됨
    # rep_image에서 흰색인 위치들에 rep_image 원소가 복사되어 colorEdge 생성
    cv2.imshow("color edge", colorEdge)

img = cv2.imread("flower.jpg", cv2.IMREAD_COLOR)
if img is None: raise Exception("영상 읽기 에러")

thresh = 50
rep_image = cv2.repeat(img, 1, 2) # 가로 반복 복사
grayImg = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환

cv2.namedWindow("color edge", cv2.WINDOW_AUTOSIZE) # 윈도우 생성
cv2.createTrackbar("Canny th", "color edge", thresh, 100, onTrackbar)
onTrackbar(thresh)	# 콜백 함수 첫 실행
cv2.waitKey(0)