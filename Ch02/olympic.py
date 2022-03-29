import turtle as t

t.setup(width=1000, height=500) # 창 크기

t.shape("turtle")
t.goto(0,0)    # 초기 위치를 0,0으로 지정
t.speed(0)
t.pensize(20)  # 펜의 크기


t.circle(100)     # 현재 위치에서 100 크기 만큼의 원을 그림

t.penup()         # 펜을 떼서 이동(그려지지 않음)
t.forward(240)    # 240만큼 앞 방향으로 이동
t.pendown()       # 펜을 갖다댐(그려짐)
t.pencolor("red") # 색을 빨간색으로 지정
t.circle(100)     # 현재 위치에서 100크기 만큼의 원을 그림

t.penup()
t.backward(480)   # 480만큼 뒤 방향으로 이동
t.pendown()
t.pencolor("blue")
t.circle(100)

t.penup()
t.right(90)     # 시계 방향으로 90도 회전
t.forward(120)  # 회전한 상태(현재 위치)에서 120 앞으로
t.left(90)      # 시계 반대 방향으로 90도 회전
t.forward(120)  # 회전한 상태(현재 위치)에서 120 앞으로
t.pendown()
t.pencolor("yellow")
t.circle(100)

t.penup()
t.forward(240)
t.pendown()
t.pencolor("green")
t.circle(100)


t.done()