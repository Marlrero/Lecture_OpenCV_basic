import cv2

IMAGE_DTYPE_MAT_TYPE = {
    "uint8":   "CV_8U",
    "int8":    "CV_8S",
    "uint16":  "CV_16U",
    "int16":   "CV_16S",
    "float32": "CV_32F",
    "float64": "CV_64F"
}

def print_matrix_info(name, image):
    matrix_type = "Unknown"
    if str(image.dtype) in IMAGE_DTYPE_MAT_TYPE.keys():
        matrix_type = IMAGE_DTYPE_MAT_TYPE[str(image.dtype)]

    n_channels = 3 if image.ndim == 3 else 1
    # 3차원이면 3, 아니면 1

    print(f'{name:12}: depth({image.dtype}), channels({n_channels}) - type({matrix_type})')

# 아래 함수에 입력을 보면 '=' 형태가 있는데,
# 이는 함수를 호출할 때 입력으로 font와 color, thickness가 없으면 '=' 옆에 있는 것이 기본값
# 각각 글꼴, 글자 색상, 굵기를 의미
def add_string_frame(frame, start_p, txt_name, txt_value,
                     font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.7,
                     color=(120, 200, 90), thickness=2):
    txt = txt_name + str(txt_value)
    shade = (start_p[0] + 2, start_p[1] + 2) # 그림자
    cv2.putText(frame, txt, shade, font, font_scale, (0, 0, 0), thickness) # 그림자
    cv2.putText(frame, txt, start_p, font, font_scale, color, thickness)

