# key, value 가 쌍으로 이루어진 map 형식 이다.
# {key1:value1, key2:value2, key3:value3 ...}

# 항목이 없는 딕셔너리 만들기
dic = dict()
print(dic)

dic = {'name': 'hong', 'phone': '010999991111', 'birth': '0202'}

# key를 호출하면 값이 나온다.
print(dic['phone'])

# 추가 하기
dic['addr'] = 'seoul'
print(dic)

# 리스트 추가
dic['hobby'] = ['축구','야구','배구','농구']
print(dic)

# 데이터 변경, key는 중복 안됨
dic['name'] = 'park'
print(dic)

# 삭제 : key를 이용해서 삭제
del dic['phone']
print(dic)

# 배구만 삭제
dic['hobby'].remove('배구')
print(dic)

