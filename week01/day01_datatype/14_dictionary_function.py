dic = {'name': 'hong', 'phone': '010999991111', 'birth': '0202'}

# keys => key 값들의 모임
dic_key = dic.keys()
print(dic_key)
# 리스트로 만들기
print(list(dic_key))

dic_value = dic.values()
print(dic_value)
# 리스트로 만들기
print(list(dic_value))

dic_item = dic.items()
print(dic_item)
# 리스트로 만들기
print(list(dic_value))

# 삭제하기(하나만 삭제)
del dic['phone']
print(dic)

# 모두 삭제하기(전체 삭제)
dic.clear()
print(dic)

dic = {'name': 'hong', 'phone': '010999991111', 'birth': '0202'}

# 데이터 얻기
print(dic['name'])
print(dic.get('phone'))

# key 가 딕셔너리 안에 있는지 조사 (in)
print('name' in dic)
print('addr' in dic)



