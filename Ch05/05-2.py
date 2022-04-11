while True:
    a=int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 3. 끝내기 : "))

    if a==1:
        b=input("*** 수식을 입력하세요 : ")
        result = eval(b)
        print(b+"의 답은 %d" % result)

    elif a==2:
        c=int(input("*** 첫 번쨰 숫자를 입력하세요 : "))
        d=int(input("*** 두 번째 숫자를 입력하세요 : "))

        sum = 0
        for i in range(c, d+1):
            sum += i
        print(f"{c}부터 {d}까지의 합은 {sum}")

    elif a==3:
        break