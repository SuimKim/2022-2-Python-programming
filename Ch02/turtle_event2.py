# import packages
import turtle
import random

# global colors: list
col = ['red', 'yellow', 'green', 'blue',
       'white', 'black', 'orange', 'pink']  # list, 형이 다른 데이터도 넣을 수 있음
print(col)
print(col[0], col[1], col[7]) # 값 뽑기 indexing
print('length =', len(col))
print(type(col))

# method to call on screen click
def fxn(x,y):
       print("Button clicked!")
       print('x =', x, 'y =', y)
       global col                 # col은 지역변수가 아니라 전역변수를 사용->global로 선언
       ind = random.randint(0,7)  # 랜덤 변수
       turtle.bgcolor(col[ind])   # 배경색을 col에서 랜덤으로 꺼내어 변경시켜줌

# windows 크기
turtle.setup(600,300)

# call method on screen click
turtle.onscreenclick(fxn, 1)  # default btn: 1->마우스 왼쪽, 2->마우스 오른쪽, 3->마우스 중간

turtle.done()




