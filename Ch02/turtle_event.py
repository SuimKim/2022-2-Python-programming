import random
import turtle as t

pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

def screenLeftClick(x,y):
    global r,g,b
    t.pencolor((r,g,b))
    t.pendown()
    t.goto(x,y)

def screenRightClick(x,y):
    t.penup()
    t.goto(x,y)

def screenMidClick(x,y):
    global r,g,b
    tSize = random.randrange(1,10)
    tutle.shap