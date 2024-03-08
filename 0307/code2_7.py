import turtle
import random

# 함수 선언 부분 #
def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))  # 현재 펜 색을 지정된 RGB 값으로 설정
    turtle.pendown()  # 펜을 내림
    turtle.goto(x, y)  # 주어진 좌표로 이동

def screenRightClick(x, y):
    turtle.penup()  # 펜을 올림
    turtle.goto(x, y)  # 주어진 좌표로 이동

def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)  # 1에서 9까지의 랜덤한 크기 선택
    turtle.shapesize(tSize)  # 거북이 모양의 크기를 설정
    r = random.random()  # 0에서 1 사이의 랜덤한 값으로 빨간색 설정
    g = random.random()  # 0에서 1 사이의 랜덤한 값으로 초록색 설정
    b = random.random()  # 0에서 1 사이의 랜덤한 값으로 파란색 설정

# 변수 선언 부분 #
pSize = 10  # 펜의 크기
r, g, b = 0.0, 0.0, 0.0  # 초기 색상 값

# 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')  # 윈도우 창의 제목 설정
turtle.shape('turtle')  # 거북이 모양 선택
turtle.pensize(pSize)  # 펜의 크기 설정

# 사용자의 마우스 클릭에 따라 각 함수가 호출되도록 설정
turtle.onscreenclick(screenLeftClick, 1)  # 왼쪽 마우스 버튼 클릭 시
turtle.onscreenclick(screenMidClick, 2)   # 가운데 마우스 버튼 클릭 시
turtle.onscreenclick(screenRightClick, 3)  # 오른쪽 마우스 버튼 클릭 시

turtle.done()  # 거북이 그림 그리기 종료

# 마우스 가운데 버튼을 클릭하면 거북이의 크기가 바뀌면서 색상이 변경됨
# 마우스 오른쪽 버튼을 클릭하면 거북이가 이동은 하지만 펜이 동작하진 않음
# 마우스 왼쪽 버튼을 클릭하면 거북이가 이동하면서 펜도 동작 (그려짐)