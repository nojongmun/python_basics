# 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
# 특징 : 중복을 허용하지 않는다. 순서가 없다. 인덱싱으로 값을 얻을 수 없다. (딕셔너리도 순서가 없다.)
# 리스트나 튜플은 순서가 없다 => 인덱싱을 통해 자료형의 값을 얻을 수 있다.

s1 = set([1, 2, 3])
print(s1, type(s1))

s2 = {1, 2, 3}
print(s2, type(s2))

s3 = set("Hello")
# 순서가 없음, 중복도 없음
print(s3)

# 리스트로 변환하기 => 인덱싱을 할 수 있다.
lis = list(s1)
print(lis, type(lis))
print(lis[1])

tu = tuple(s1)
print(tu, type(tu))
print(tu[1])

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 (중복된 갓은 한 개씩만 표현된다.)
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s2 - s1)

print(s1.difference(s2))
print(s2.difference(s1))

# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#  값 여러개 추가하기(update)
s1.update([3, 4, 5, 6])
print(s1)

# 값 제거 하기(remove)
s1.remove(3)
print(s1)

# 전체 삭제(clear)
s1.clear()
print(s1)






