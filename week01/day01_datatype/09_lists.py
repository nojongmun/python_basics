# Lists : 대괄호 사이에 쉼표로 구분된 값(항목)의 목록, (베열과 비슷)
# 서로 다른 유형의 항목이 포함될 수 있지만, 일반적으로 모든 항목이 동일한 유형을 갖는다.
# 리스트명 = [ 요소1, 요소2, 요소3, ... ]
odd = [1, 3, 5, 7, 9]

# 인덱싱과 슬라이싱이 가능하다. => 결과는 리스트
print(odd)
print(odd[0])
print(odd[-1])
print(odd[:2])
print(odd[3:])

# 서로 다른 유형의 항목
even = [2, 4, 6, 'my', 'love', 8, 'you', 10]
print(even)
print(even[2:7])

# 리스트 안에 리스트
even2 = [2, 4, 6, odd, 8, 10]
print(even2)
print(even2[2], type(even2[2]))                   # int
print(even2[3], type(even2[3]))                   # list
print(even2[3][0], type(even2[3][0]))             # int
print(even2[3][0:3], type(even2[3][0:3]))         # list
