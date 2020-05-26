str1 = "hello python"
str2 = "HELLO PYTHON"

# capitalize() : 첫글자 대문자 나머지 소문자
print(str1.capitalize())

# casefold() : 소문자로 만들기
# lower() : 소문자로 만들기
print(str2.casefold())
print(str2.lower())

# 대문자로 만들기
print(str1.upper())

# count('문자') : 선택된 문자의 갯수 세기
print(str1.count('o'))
print(str2.count('o')) # 대소문자를 구분함

# find : 위치값(index) 알려주기
str3 = "Python is best choice"
print(str3.find('b'))
print(str3.find('k'))  # 없을때는 -1

print(str3.index('b'))
# print(str3.index('k'))  # 없을때는 오류 발생

# 문자열 삽입 : '삽입문자'.join('대상문자열')
print('*'.join(str3))

# 공백지우기 : strip(양쪽) , lstrip(왼쪽), rstrip(오른쪽)
str4 = '   hi   '
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())

# 길이 구하기 : len
print(len(str4.strip()))
print(len(str4.lstrip()))
print(len(str4.rstrip()))

# 문자 치환 : replace ,
str5 = "Pithon"
str6 = str5.replace("Pi", "Py")
print(str6)

str7 = "Pithon Pithon Pithon"
print(str7.replace("Pi", "Py"))

# 문자열 나눈기 : split = > 결과가 리스르라는 자효형으로 출력됨
print(str7.split(" "))

