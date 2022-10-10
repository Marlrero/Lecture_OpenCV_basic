import numpy as np, cv2

image = cv2.imread("pyramid.jpg", cv2.IMREAD_COLOR)    # 로고를 붙일 백그라운드 영상
logo  = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)       # 로고 영상
if image is None or logo is None: raise Exception("영상 파일 오픈 에러")
cv2.imshow("origin_image", image)
cv2.imshow("origin_logo", logo)

# 이미지 logo에 대해 220 픽셀보다 크면, 255 픽셀로 바꾸고, 작다면 0으로 바꿔라 (이진화, 문턱기준)
masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks) # 3채널로 분리

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])       # 포어그라운드(전경) 통과 마스크: B or G
cv2.imshow("B or G", fg_pass_mask)
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)   # 포어그라운드(전경) 통과 마스크: B or G or R
cv2.imshow("B or G or R", fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)            # 포어그라운드 마스크를 비트 반전시킴
cv2.imshow("not (B or G or R)", bg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2]        # 백그라운드, 로고 영상 크기
x, y = (W - w) // 2, (H - h) // 2    # 백그라운드의 중심, 로고의 중심 조정
roi = image[y:y+h, x:x+w]            # 관심 영역(roi) 지정

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask) # 로고의 전경 복사
cv2.imshow("forground", foreground)
background = cv2.bitwise_and(roi, roi , mask=bg_pass_mask) # roi에 원본배경만 복사
cv2.imshow("background", background)

dst = cv2.add(background, foreground) # 로고 전경과 원본 배경 간 합성
cv2.imshow("dst", dst)

image[y:y+h, x:x+w] = dst             # 합성 영상을 원본에 복사
cv2.imshow("image", image)

cv2.waitKey()