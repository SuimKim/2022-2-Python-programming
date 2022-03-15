import turtle as t

t.setup(width=1000, height=500)

t.shape("turtle")
t.goto(0,0)
t.speed(0)
t.pensize(20)


t.circle(100)

t.penup()
t.forward(240)
t.pendown()
t.pencolor("red")
t.circle(100)

t.penup()
t.backward(480)
t.pendown()
t.pencolor("blue")
t.circle(100)

t.penup()
t.right(90)     #시계 방향으로 90도 회전
t.forward(120)  #회전한 상태에서 120 앞으로
t.left(90)      #시계 반대 방향으로 90도 회전
t.forward(120)  #그 위치에서 120 앞으로
t.pendown()
t.pencolor("yellow")
t.circle(100)

t.penup()
t.forward(240)
t.pendown()
t.pencolor("green")
t.circle(100)


t.done()