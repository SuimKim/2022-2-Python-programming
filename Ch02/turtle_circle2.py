import turtle as t

t.shape("turtle")
t.color("green")
t.speed(5)

r=int(input("몇 개의 원을 그릴까요?"))

for i in range(r):
    # 반지름 100으로 원 그리기
    t.circle(100)
    # 360/r 각도 이동
    t.left(360/r)
    t.forward(20)

t.done()