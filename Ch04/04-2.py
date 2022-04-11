import turtle
import random

def turtleMove(x, y):
    global r,g,b

    r = random.random()
    g = random.random()
    b = random.random()                 # 8-10 랜덤 색상값
    turtle.color((r, g, b))             # 거북이 색상을 랜덤으로

    turtle.pendown()
    turtle.goto(x,y)

# 변수 선언
r, g, b = 0.0, 0.0, 0.0
x, y = 0, 0
swidth = 300
sheight = 300

# 코드 작성
turtle.setup(swidth, sheight)

turtle.shape('turtle')

for _ in range(0,50):
    x = random.randrange(-500, 500)
    y = random.randrange(-500, 500)
    turtleMove(x, y)

turtle.done()