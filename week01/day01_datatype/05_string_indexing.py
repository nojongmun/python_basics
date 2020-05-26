# 인덱싱과 슬라이싱
# 인덱싱 : '가리킨다.'
# 슬라이싱 : '잘라낸다.'

# 인덱싱
str = "Hello Python"

# 왼쪽에서 오른쪽으로 , 0부터 시작
print(str[0])
print(str[11])
print('-'*20)

# 오른쪽에서 왼쪽으로, -1부터 시작
print(str[-1])
print(str[-12])
print('-'*20)

# 슬라이싱 : 원하는 위치에서 원하는 갯수만큼만 추출
# 시작위치:끝위치(포함안됨),
print(str[0:5])
print(str[6:12])
print('-'*20)

# 시작위치:생략   , 생략:끝위치
print(str[:5])
print(str[6:])
print('-'*20)

# 그냥 처음부터 끝까지
print(str)
print(str[:])
print('-'*20)

# 예제
str = "20200416121240"
date = str[:8]
time = str[8:]

year = date[:4]
month = date[4:6]
day = date[6:]
print(year+"년 "+month+"월 "+day+"일")
print('-'*20)

# 틀린 글자 변경하기
# 오류 발생 : 문자열은 불변형(변경이 불가능한 데이터 성질)이므로 추가, 삭제, 수정이 불가능
# 가변형 자효형 :  list, dict, set  => 추가, 삭제, 수정 할 수 있는 메소드가 존재
# 불변형 자료형 : str, tuple
str = "Pithon"
# str[1] = "y"
# print(str)

print(str[:1]+"y"+str[2:])
