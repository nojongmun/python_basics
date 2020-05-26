# 리스트는 여러 요소들을 갖는 컬렉션
# 요소를 추가하거나 삭제, 갱신이 가능함
# 동적 배열 구조로 자유롭게 확장, 축소가 가능한 구조 (mutable data type)
# 한가지 타입으로 구성된 리스트, 여러 타입으로 구성된 리스트

lst = [1,2,3,4,5, '뽀로로']

for i in lst:
    print(i, end=' ')
print()
# append() : 리스트에 요소를 추가하는 함수
lst.append('루피')
lst.append(['에디', '패티'])
lst.append('뽀로로')
lst.append(5)
# 리스트는 데이터의 중복 허용, 순서 유지

# insert() : 추가.. 삽입 ,
lst.insert(2, '뽀로로')
lst.insert(6, 6)

# extend() :데이터 추가 , 묶음으로 추가되지 않고 1개씩 추가됨
lst.extend(['뽀로로1', '뽀로로2', '뽀로로3'])

print(lst.index('뽀로로')) # 요소의 인덱스 번호

print(lst.count('뽀로로')) # 요소의 갯수

lst.remove('뽀로로') # 삭제, 요소가 여러 개 인경우 앞에서 부터 삭제

lst.remove(5)  # 객체의 값으로 삭제
lst.remove(5)


# 리스트의 마지막에서 한개 꺼내기
print(lst.pop()) # 디폴트 매개변수는 -1
print(lst.pop(10))

print(lst)

lst1 = [1,6,2,4,3,5]
# sort() : 정렬 함수
print(lst1)
lst1.sort()  # 원본 데이터에 액세스 후 수정
print(lst1)

# 반전 함수
lst1.reverse()
print(lst1)





















