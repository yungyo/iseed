import turtle  # 거북이 모듈 불러오기
import random  # 난수 생성 모듈 불러오기
from tkinter import Tk, simpledialog  # Tkinter에서 Tk 객체와 simpledialog 모듈 불러오기
import math  # 수학 함수 모듈 불러오기

# Tkinter의 루트 창 생성 및 숨기기
root = Tk()
root.withdraw()

# 거북이 초기화
turtle.setup(width=500, height=500)  # 화면 크기 설정
turtle.shape('turtle')  # 거북이 모양 설정
turtle.penup()  # 펜을 올려서 그리지 않게 설정

# 사용자로부터 문자열 입력 받기
inStr = simpledialog.askstring('문자열 입력', '거북이가 쓸 문자열을 입력')

# 초기 설정
radius = 200  # 나선 모양의 초기 반지름
txtSize = 20  # 문자의 크기

# 입력된 문자열의 길이 구하기
num_chars = len(inStr)

# 문자열의 각 문자가 나타날 각도 계산
angle_per_char = (360 * 2) / (num_chars)

# 각 문자열에 대해 나선 모양으로 문자 그리기
for i, ch in enumerate(inStr):
    # 문자가 그려질 위치를 계산하기 위해 각도 계산
    angle = i * angle_per_char

    # 나선 모양으로 문자를 배치하기 위해 반지름 계산
    spiral_radius = radius - (3 * i)

    # 삼각함수를 이용하여 문자가 그려질 위치 계산
    x = spiral_radius * math.cos(math.radians(angle))
    y = spiral_radius * math.sin(math.radians(angle))

    # 거북이를 문자가 그려질 위치로 이동
    turtle.goto(x, y)

    # 무작위로 색상 선택
    r, g, b = random.random(), random.random(), random.random()
    turtle.pencolor((r, g, b))

    # 선택한 글꼴과 크기로 문자 출력
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

# 모든 문자를 그린 후에는 거북이 그래픽 창이 유지되도록 설정
turtle.done()
