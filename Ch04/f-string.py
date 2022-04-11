a = 'happy'
b = 'love'
print(f'a = {a} b = {b}')                      # f-string
print('a = {0} b = {1}'.format(a,b))           # 위치인자
print('a = {k1} b = {k2}'.format(k1=a, k2=b))  # 키워드인자

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. I am {family} {name}')


print("hello")
print('\hello')

print("I don't know")
print('I don\t know')

print(r'c:\usr\bin')

print("""\
line1
line2
line3\
""")

print("""aaaaaaaaaaaa
        bbbbbbbbbbbbbbb
""")
