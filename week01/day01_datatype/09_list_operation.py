# 리스트 연산자

# 리스트 더하기 ( + ) :
su1 = [1, 2, 3]
su2 = [100, 200, 300, 400, 500]
str1 = ['my', 'python', 'love']
print(su1 + su2)
print(su2 + str1)

print(su1[0]+su2[0])  # 101
# print(su1[0]+str1[0])  # 오류발생
print(str(su1[0])+str1[0])  # 성공 : 정수, 실수 를 string 으로 형 변환 =>  str(int)

# 리스트 곱하기 ( * ) : 리스트 내용 반복 하기
print(su1 * 3)
print(str1 * 3)

# 리스트 수정, 변경, 삭제
# 요소 하나 수정  => string 과 튜플은 안됨
su1[1] = 4
print(su1)

# 요소 여러개 수정 => index 1-2 자리에 요소 대신에 'a', 'b', 'c' 로 변경한다는 말임 : [1, 'a', 'b', 'c', 3]
su1[1:2] = ['a', 'b', 'c']
print(su1)

su1[1:3] = ['A', 'B', 'C']
print(su1)

# 주의 사항 : index 1의 자리에  [100, 200, 300]가 들어감 : [1, [100, 200, 300], 'B', 'C', 'c', 3]
su1[1] = [100, 200, 300]
print(su1)

# 리스트 요소 삭제
su1[3:4] = []
# [1, [100, 200, 300], 'B', 'c', 3]
print(su1)

# [1, [100, 200, 300], 'B', [], 3]
# 삭제 안됨
su1[3] = []

# del  사용하기 :
del su1[3]
print(su1)

# 복사하기 : 주의 사항) 원본이 변경되면 , 복사본도 변경된다.
su2 = su1
print(su1)
print(su2)

# id는 변수의 메모리 주소값을 리턴한다.
# su1, su2가 같은 주소값을 가지고 있다. => 데이터가 변경되어도 주소값은 같다. (가변형(주소에 있는 내용이 변경 된다.=call by reference 속성))
# 그러므로 원본(복사본)이 변경되면 , 복사본(원본)도 변경된다.
print(id(su1))
print(id(su2))
print('-'*15)

# 실패
su1[1:2][1:2] = []
print(su1)
print(su2)
print('-'*15)

su1[1][1] = []
print(su1)
print(su2)

del su2[1][1]
print(su1)
print(su2)

del su1[1:2]
print(su1)
print(su2)

su2[1] =['A', 'B', 'C']
print(su1)
print(su2)



