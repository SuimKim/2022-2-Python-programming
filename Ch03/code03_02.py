# 서식 출력
print("%d %d %d" % (100,200,300))
print("x=%d y=%5d z=%05d" % (100,200,300))

# format 함수 위치 인자
print("{0:d} {1:5d} {2:05d}".format(100,200,300))
print("{1:5d} {0:d} {2:05d}".format(100,200,300))

# format 함수 키워드 인자
print("{a}, {b}, {c}".format(a=100,b=200,c=300))


# using format() method
print('I love {} for "{}!"'.format('Python', 'Coding'))
print('{0} and {1}'.format('Python', 'Java'))
print('{a} and {b}'.format(a='Python', b='Java'))

# 다양한 특수 문자
print("\n줄바꿈\n연습")
print("\t탭키\t")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")