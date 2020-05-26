
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





