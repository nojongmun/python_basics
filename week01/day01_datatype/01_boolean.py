# 자료형(DataType) : 해당 프로그램에서 사용(처리)하는 자료들의 타입(종류)를 말한다.
# 자료형의 종류: 숫자형(numeric), 문자열(string), 불린(boolean), 리스트(list), 튜플(Tuple), 딕셔너리(dictionary), 집합(Set)
# 파이썬(Python)에서는 변수 선언시 정확하게 데이터 타입의 선언할 필요가 없다. 이 형태는 동적 타이핑(dynamic typing)으로 알려져 있다.

# boolean : 참 / 거짓,  조건식에 가장 많이 사용된다.
# 참일때는 True, 거짓일때는 False
con = True
print(con)

con = False
print(con)

# 대소문자를 구분한다.
# con = true
# con = false

print('-'*20)
# 숫자 : 0이 아니면 True, 0 이면 False
su1 = 10
print(bool(su1))
su2 = 0
print(bool(su2))

# 문자 : 데이터가 있으면 True, ""이면 False
str1 = "Python"
print(bool(str1))
str2 = ""
print(bool(str2))

# 리스트 : 데이터가 있으면 True, ""이면 False
lst1 = [1, 2]
print(bool(lst1))
lst2 = []
print(bool(lst2))

# tuple  : 데이터가 있으면 True, ""이면 False
tup1 = (1,2)
print(bool(tup1))
tup2 = {}
print(bool(tup2))

# dictionary  : 데이터가 있으면 True, ""이면 False
dic1 =  {'name': 'hong', 'phone': '010999991111', 'birth': '0202'}
print(bool(dic1))
dic2 = {}
print(bool(dic2))

# set  : 데이터가 있으면 True, ""이면 False
set1 = set([1, 2, 3])
print(bool(set1))
set2 = set([])
print(bool(set2))