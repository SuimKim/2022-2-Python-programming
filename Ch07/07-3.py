singer = {}

singer['이름']='트와이스'
singer['구성원수']=9
singer['데뷔']='서바이벌 식스틴'
singer['대표곡']='SIGNAL'

for k in singer.keys():
    print('%s-->%s' % (k, singer[k]))

for k in singer.items():
    print(k)

for i, j in singer.items():
    print(f'{i}:{j}')

print(singer.keys())
print(singer.items())