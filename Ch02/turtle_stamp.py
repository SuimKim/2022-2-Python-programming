import turtle
import random

# 함수 선언
def screenLeftClick(x, y):
    tSize = random.randrange(2, 10)     # 거북이 사이즈 랜덤값(2~10의 범위를 지정)
    turtle.shapesize(tSize)             # 스탬프 사이즈를 tSize로 지정
    r = random.random()
    g = random.random()
    b = random.random()                 # 8-10 랜덤 색상값
    turtle.color((r, g, b))             # 거북이 색상을 랜덤으로
    tAngle = random.randrange(0, 360)   # 거북이가 회전하는 각도의 랜덤값(0~360도의 범위 지정)

    turtle.penup()        # 펜을 떼서 이동(이동하는 동안 그려지지 않음)
    turtle.goto(x, y)     # 마우스로 클릭할 x, y 좌표로 이동
    turtle.left(tAngle)   # 왼쪽 방향으로, tAngle만큼 회전
    turtle.stamp()        # 현재 위치에서 거북이 스탬프를 찍음

# 코드 작성
tSize, tAngle = 0,0   # 초기 크기, 각도 지정

turtle.title('거북이 도장 찍기')
turtle.shape('turtle')

turtle.onscreenclick(screenLeftClick,1)  # 위에 선언한 함수를 1번=마우스 왼쪽을 누르면 실행

turtle.done()
