import turtle
import random

turtle.speed(70)
width = 550
height = 550
turtle.shape('turtle')
turtle.screensize(500, 500)
turtle.setup(550,550)
turtle.penup()
turtle.goto(0, -height/2)
turtle.pendown()

for i in range(0, 250):
    ran = random.randrange(0, 6)
    if ran==0:
        turtle.pencolor("red")
    elif ran == 1:
        turtle.pencolor("orange")
    elif ran == 2:
        turtle.pencolor("yellow")
    elif ran == 3:
        turtle.pencolor("green")
    elif ran == 4:
        turtle.pencolor("blue")
    elif ran == 5:
        turtle.pencolor("purple")

    turtle.circle(i)



turtle.done()



