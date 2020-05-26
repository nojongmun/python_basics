# 컬렉션 , 자료구조 ==> list, set, dictionary, tuple
# Set : 집합 , 중복허용x , 순서 유지 x

myset = {1, 2, 3}

myset.add(3.0)
myset.add("one")
myset.add(2)
myset.add(float(4))
myset.add(4.00)
myset.add(2)
myset.add(int(2))

print(myset)

if myset.__contains__(1):
    print('있어요')
else:
    print('없어요')































