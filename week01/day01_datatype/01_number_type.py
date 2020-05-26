# https://docs.python.org/ko/3.7/  참조하기
# https://wikidocs.net/book/1  점프 투 파이썬

# 주석표현은 #으로 표시한다.
# 자료형(DataType) : 해당 프로그램에서 사용(처리)하는 자료들의 타입(종류)를 말한다.
# 자료형의 종류: 숫자형(numeric), 문자열(string), 불린(boolean), 리스트(list), 튜플(Tuple), 딕셔너리(dictionary), 집합(Set)
# 파이썬(Python)에서는 변수 선언시 정확하게 데이터 타입의 선언할 필요가 없다. 이 형태는 동적 타이핑(dynamic typing)으로 알려져 있다.
# 타입을 알아보는 명령어 : type(대상)

# 숫자 자료형
# 정수형 글꼴
age = 123
print(age, type(age))

# 실수형
weight = 98.7
print(weight, type(weight))

# 실수형 지수
height = 1.8012E2
print(height, type(weight))

# 8진수와 16진수
num = 0o10
print(num,type(num))

num = 0o11
print(num,type(num))

num = 0x10
print(num,type(num))

num = 0x20
print(num, type(num))

# 복소수
num = 12+2j
print(num, type(num))
# 실수부분 출력
print(num.real, type(num.real))
# 허수 부분 출력
print(num.imag, type(num.imag))
# 컬레복소수(허수부분의 부호 변경
print(num.conjugate(), type(num.conjugate()))





