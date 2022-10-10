import numpy as np, cv2

def morphing():
    h, w = image.shape[:2]
    dst = np.zeros((h, w), image.dtype)
    ys = np.arange(0, image.shape[0], 1) # 간격 1
    xs = np.arange(0, image.shape[1], 0.1)  # 간격 0.1  (가로 방향 왜곡 값 10배 세밀하게 하기 위함)

    x1, x10 = pt1[0] , pt1[0]*10 # 클릭된 x좌표 x1, 클릭 x좌표를 0.1 간격으로 구성한 xs 행렬 인덱싱 위함
    ratios = xs / x1  # 각 x좌표에 대해 변경 비율들을 계산해서 행렬 생성
    ratios[x10:] = (w - xs[x10:]) / (w - x1)
      # 클릭 좌표 이후의 x좌표에 대한 변경 비율 계산
      # (x좌표 인덱스가 10배만큼 만들어졌으므로, x10에서 마지막 범위까지 할당)

    dxs = xs + ratios * (pt2[0] - pt1[0]) # x좌표 변경 인덱스 계산
    xs, dxs = xs.astype(int), dxs.astype(int)

    ym, xm = np.meshgrid(ys, xs) # 좌표 인덱스로 정방행렬 생성 (원본)
    _, dxm = np.meshgrid(ys, dxs) # 변경된 좌표
    dst[ym, dxm] = image[ym, xm] # 원본을 변경좌표로 매핑
    cv2.imshow("image", dst)

def onMouse(event, x, y, flags, param):
    global pt1, pt2
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x, y)                               # 드래그 시작 좌표
    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x, y)                               # 드래그 종료 좌표
        morphing()                                 # 드래그 종료 시 워핑 변환 수행
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        pt1 = pt2 = (-1, -1)
        cv2.imshow("image", image)                 # 오른쪽 버튼 더블 클릭 시 원복

image = cv2.imread('chessboard.png', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 읽기 에러")

pt1 = pt2 = (-1, -1)
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)          # 마우스 콜백 함수 등록
cv2.waitKey(0)