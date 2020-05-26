# 주석표현은 #으로 표시한다.
# https://docs.python.org/ko/3.7/  참조하기
# https://wikidocs.net/book/1  점프 투 파이썬

# 변수 : 데이터(값)를 저장하는 공간,
#       객체를 가리키는 것, 객체란 파이썬에서 사용된느 모든 것

# 변수명 = 변수에 저장할 데이터 ( 자바와 c언어 처럼 자료형을 정의할 필요가 없음)
# su = 3
# 3 이라는 데이터를 가진 정수 자료형이 자동으로 메모리엥 생성 된다.
# 3 이라는 정수형 객체가 저장된 메모리 위치를 가리키게 된다.
# 이렇게 데이터의 메모리 위치를 가리키는 것을 레퍼런스(참조)라고 한다.

su = 3

# 콘솔창에 su 라는 변수가 가지고 있는 데이터를 출력하라
print(su)
# 타입을 알아보는 함수 : type(대상)
print(type(su))

num = 3
print(su)
print(type(su))

# is  동일한 객체를 가르키는지 판단하는
print(su is num)

# 메모리에 변수을 삭제하자 : del
del(su)

# name 'su' is not defined
# print(su)

#