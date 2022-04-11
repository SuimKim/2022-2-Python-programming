d = {'apple':1, 'melon':2, 'mango':3}

print(d['apple'])

print("-----key 값 출력")
for i in d.keys():
    print('key = %s' %(i))
print("-----value 값 출력")
for i in d.keys():
    print('value = %s' %(d[i]))
print("-----key, value 값 출력")
for i in d.keys():
    print('key = %s, value = %d' %(i, d[i]))