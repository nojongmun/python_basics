# if문 : 조건식이 참일때와 거짓을때 각각 나눠서 처리하다.

# if 조건식:
#       조건식이 참일때 실행할 문장;
#       조건식이 참일때 실행할 문장;
# else:
#       조건식이 거짓일때 실행할 문장;
#       조건식이 거짓일때 실행할 문장;

# money 가 있으면 택시를 타고 아니면 걸어가자
money = 1000
res = ""
if money:
    res = "택시를 타자"
else:
    res = "걸어가자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

money = 0
res = ""
if money:
    res = "택시를 타자"
else:
    res = "걸어가자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

# money 가 10000이상 있으면 택시를 타자
money = 10000
res = ""
if money >= 10000:
    res = "택시를 타자"
else:
    res = "걸어가자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

money = 8000
res = ""
if money >= 10000:
    res = "택시를 타자"
else:
    res = "걸어가자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

#  money 가 10000이상 있거나 card가 있으면 택시를 타자
money = 8000
card = 1
res = ""
if money >= 10000 or card:
    res = "택시를 타자"
else:
    res = "걸어가자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

money = 8000
card = 0
res = ""
if money >= 10000 or card:
    res = "택시를 타자"
else:
    res = "걸어가자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

# 다른 프로그램에서 흔히 볼수 없는 것 ( in,  not in)
# 해당 리스트에 7이 존재하냐
if 4 in [1, 2, 3, 4, 5, 6]:
    print("list 존재함")
else:
    print("존재않함")

print("수고 하셨습니다.")
print('-'*30)

# 해당 튜플에 4이 존재하냐
if 4 in (1, 2, 3, 4, 5, 6):
    print("tuple 존재함")
else:
    print("존재않함")

print("수고 하셨습니다.")
print('-'*30)

# 해당 set에 2이 존재하냐
if 2 in set([1, 2, 3]):
    print("set 존재함")
else:
    print("존재않함")

print("수고 하셨습니다.")
print('-'*30)

# 해당 딕셔너리 안에 key 값 중에 name이 존재하냐
if 'name' in {'name': 'hong', 'phone': '010999991111', 'birth': '0202'}:
    print("dic 존재함")
else:
    print("존재않함")

print("수고 하셨습니다.")
print('-'*30)

# 해당 구간을 그냥 지니가고 싶을 때
if 'name' in {'name': 'hong', 'phone': '010999991111', 'birth': '0202'}:
    pass
else:
    print("존재않함")

print("수고 하셨습니다.")
print('-'*30)

# num 이 홀수인지 짝수인지 판별하자
num = 242
res = ""
if num % 2 == 0:
    res = "짝수"
else:
    res = "홀수"

print(res)
print("수고 하셨습니다.")
print('-'*30)