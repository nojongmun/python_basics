# 딕셔너리 메서드

dic={101:'둘리', 201:'도우너', 301:'마이콜', 401:'또치'}
# get(key)  :  value 데려오기, 값이 없으면 None출력
print(dic.get(102))

print('dic items() : ', dic.items())

# -------------------------------------
# keys() : 키 리스트 만들기
dict_emp={'name':'뽀로로','phone':'010-1234-5678', 'addr':'강남구'}
print(dict_emp.keys())
# key=dict_emp.keys()
# print('키 목록 : ', key)
# print(type(key))

# 키 출력 1---------
for key in dict_emp.keys():
    print('키 : ', key)

# 키 출력 2---------
key = dict_emp.keys()
for k in key:
    print('키 : ', k)
# print(type(key))

# 키 출력 3---------
key = list(dict_emp.keys())
print(key)  # ['name', 'phone', 'addr']
print(type(key))  # class 'list'

# -------------------------------
# 밸루 출력1--------------
for v in dict_emp.values():
    print('밸루 : ', v)

# 밸루 출력2--------------
value=dict_emp.values()
for v in value:
    print(v)

# 밸루 출력3--------------
value = list(dict_emp.values())
print(value)

# --------------------------------------------

# 키로 밸루 얻기
print('get() 사용 : ', dict_emp.get('name')) # 찾는 값이 없으면 None리턴
print('[] 사용 : ', dict_emp['name']) # 찾는 값이 없으면 아무것도 출력하지 않음

print(dict_emp.get('name1', '찾는 값이 없어요'))

# 해당 키가 딕셔너리에 있는지 조사(in)
print('name' in dict_emp) # 키가 있으니 True
print('dic' in dict_emp) # 키가 없으니 False

# clear() : 키 밸루 쌍 모두 지우기
dict_emp.clear()
print(dict_emp)

print('-'*30)
# 값으로 키 찾기----------------------

mydict = {'harry':20, 'luna':20}
sch_age = int(input('찾고 싶은 나이를 입력하세여  : '))

for name, age in mydict.items():
    if age==sch_age:
        print(name)

# 딕셔너리 컴프리헨션
[print(name) for name, age in mydict.items() if age==sch_age]




































