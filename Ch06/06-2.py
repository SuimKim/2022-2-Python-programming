import random

tries = 0   # 시도 횟수
guess = 0   # 사용자의 추측값
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer:
    if tries >= 10:
        break
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("너무 낮음")
    elif guess > answer:
        print("너무 높음")


if guess == answer:
    print("축하합니다. 시도횟수=", tries)
else:
    print("10번 내에 정답 실패, 정답은", answer)
