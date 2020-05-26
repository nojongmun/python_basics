# tuple은 리스트와 비슷하게 여러 요소를 갖는 컬렉션
# tuple은 새로운 요소를 추가하거나 갱신, 삭제 할수 없음(immutable data type)
# list는 [] 생성, tuple은  ()를 이용하여 생성
# 값의 변화가 불가능한 부분을 제외하고 리스트와 동일

tp = ()  # 빈 튜플 생성
tp = (1,2,3,4,5,6,7,8,9,10)

# print(type(tp))
print(tp)

# ↓ int형의 자료로 인식
tp1 = (10*2)
print(type(tp1))
print(tp1)
# -------------------

# ↓ tuple형의 자료로 인식
tp2 = (10,)
print(type(tp2))
print(tp2)
# -------------------------

t1 = (1,2,'뽀로로','크롱','뽀로로','루피')
print(t1)

# del t1['크롱']  # 삭제를 지원하지 않음
# print(t1)

print(t1.index('뽀로로')) # 2번째 방 !!

print(t1.count('뽀로로')) # '뽀로로'가 2개

# tup=(1,5,3,7,8,6,4,2,10,9)
# tup.sort() # 에러 , 갱신불가
# print(tup)






















