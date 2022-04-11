l=['apple', 'banana', 'mango']

print("리스트 길이:", len(l))
print("0번째 인덱스:", l[0])

l.append('melon') # 맨 뒤에 항목 추가

print(l.pop())  # 마지막 항목 빼내기
print(l.pop())  # 마지막 항목 빼내기

for i in l:
    print(i)