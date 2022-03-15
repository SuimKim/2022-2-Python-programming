import turtle as t
# 윈도우 크기
# t.screensize(10,10, bg="yellow")

# 캔버스 크기
t.setup(width=500, height=500)


t.shape('turtle')
t.pensize(10)
t.color("red")
t.bgcolor("yellow")
t.fillcolor("blue")

t.penup()
t.goto(0,0)
t.pendown()

t.begin_fill()
for i in range(0,4):
    t.forward(200)
    t.right(90)
t.end_fill()

t.done()
