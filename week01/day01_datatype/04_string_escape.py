# 이스케이프 문자
#  \n : 개행(줄바꿈)
#  \t : 탭(일정 간경 띄우기)
#  \" : 큰따옴표 출력 (")
#  \' : 작은따옴표 출력(')
#  \\ : 문자 \ 를 그대로 출력

str = "안녕하세요\nHello\n반갑습니다."
print(str)

str = "안녕하세요\tHello\t반갑습니다."
print(str)

str = "\'안녕하세요\' \'Hello\' \'반갑습니다.\'"
print(str)

str = "\"안녕하세요\" \"Hello\" \"반갑습니다.\""
print(str)

# 문자열 더하기
str = "Hello" + "Python"
print(str)

# 문자열 곱하기
str = "Python"
print(str * 3)