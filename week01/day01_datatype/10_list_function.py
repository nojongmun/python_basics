# 리스트 요소 추가 하기 (append)
su1 = [1, 3, 2]
print(su1)

su1.append(4)
print(su1)

su1.append('A')
print(su1)

su1.append([2, 'B'])
print(su1)

# 정렬 (sort)
su2 = [1, 5, 9, 4, 3, 8]
su2.sort()
print(su2)

su3 = ['a', 'c', '가', '나', 'e', '#', '!', '※']
su3.sort()
print(su3)

# 오류 발생
su4 = [1, 5, 'a', 9, 4, 'c', 3, 8]
print(su4)

# 'str' 과 'int'의 인스턴스간의 < (관계연산) 을 지원하지 않음
# su4.sort()
# print(su4)
print('-'*20)

# 리스트 뒤집기 (reverse)
su2.reverse()
print(su2)

su3.reverse()
print(su3)
print('-'*20)

su5 = [1, 5, 9, 4, 3, 8]
su5.sort(reverse=True)
print(su5)

su5.sort(reverse=False)
print(su5)

su6 = ['a', 'c', '가', '나', 'e', '#', '!', '※']
su6.sort(reverse=False)
print(su6)

su6.sort(reverse=True)
print(su6)

# 데이터의 위치 값 얻기 (index(데이터))
num = [1, 2, 3, 4]
print(num[2])
print(num.index(3))

# 없은 데이터의 위치값은 오류 발생
# print(num.index(5))
