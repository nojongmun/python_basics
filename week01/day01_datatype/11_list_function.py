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
print(num[2])         # index가 2인 데이터의 값 리턴
print(num.index(3))   # 데이터가 3인 위치값 리턴

# 없은 데이터의 위치값은 오류 발생
# print(num.index(5))

# 요소 삽입 (insert)
num = [1, 2, 3]
num.append(4)
print(num)
num.insert(0, 4)
print(num)

# 요소 삭제 (remove(데이터))
# num.remove(0)  # 0 데이터 없으므로 삭제
# print(num)

# 첫번째 나오는 4를 삭제
num.remove(4)
print(num)

# 마지막 요소 삭제하하기 (pop) => 삭제된 요소 저장 가능 (remove 는 삭제만 가능)
num2 = num.pop()
print(num)
print(num2)

# 리스트에 포함된 요소의 갯수 : count(데이터)
num = [1, 2, 3, 1, 2, 1]
print(num.count(1))

# 리스트에 리스트 추가 하기 : extend(요소로 추가됨)
num.append(['a', 'b'])
print(num)

num.extend(['a', 'b'])
print(num)
