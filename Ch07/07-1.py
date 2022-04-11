foods = {"떡볶이":"오뎅", "짜장면":"단무지", "라면":"김치"}
print(foods)

# 모든 key를 가져오기
print(foods.keys())

for key in foods.keys():
    print('key =',key, 'value=',foods.get(key))

print(foods.get("짜장면"))