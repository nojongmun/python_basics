# 보통 값의 변동이 발생하는 경우가 많으므로 튜플보다 리스트를 선호
# 튜플은 주로 함수에서 여러개의 값을 반환할 경우 가장 유익하게 사용

# 튜플 변수 할당
name = ('뽀', '로로')
print(name)

# last_name, first_name=('뽀', '로로') # 튜플의 내용을 분리하여 변수에 할당 가능
# print(last_name, first_name)
last_name, first_name=name # 튜플의 내용을 분리하여 변수에 할당 가능
print(last_name, first_name)

# TC :튜플 컴프리헨션
tc=tuple(n**2 for n in range(10) if n%2==0) # 튜플로 인식
# tc=(n**2 for n in range(10))  # 객체의 참조 주소만 리턴
print(tc)
print(type(tc))

# for n in range(10):   # 14라인과 동일
#     if n%2==0:
#         print(n^2)

# 페어로 묶어서 전달
a = (1,2,3,4,5)
b = ('a','b','c','d','e')

for x, y in zip(a, b):
    print(x, y)































