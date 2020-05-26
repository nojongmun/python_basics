# 단순 if문 : 조건식이 참일때만 실행, 거짓이면 if문 무시

# if 조건식:
#    조건식이 참일때 실행할 문장;
#    조건식이 참일때 실행할 문장;

# 주의 사항 : 들여쓰기를 해야 하고 일정해야 한다.
# switch, case 라는 키워드가 존재하지 않습니다.(나중에 함수와 딕셔너리를 이용해서 비슷하게 만들 수는 있음)

# 조건식에는 boolean 형, 비교연산, 논리연산을 사용한다.
# boolean 형-> True, False,
# 비교연산 ->  >, >=, ==, !=, <, <=  (결과가 boolean 형)
# 논리연산 -> and, or, not  (결과가 boolean 형)

# money 가 있으면 택시를 타자
money = 1000
res = ""
if money:
    res = "택시를 타자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

money = 0
res = ""
if money:
    res = "택시를 타자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

# money 가 10000이상 있으면 택시를 타자
money = 10000
res = ""
if money >= 10000:
    res = "택시를 타자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

money = 8000
res = ""
if money >= 10000:
    res = "택시를 타자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

#  money 가 10000이상 있거나 card가 있으면 택시를 타자
money = 8000
card = 1
res = ""
if money >= 10000 or card:
    res = "택시를 타자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

money = 8000
card = 0
res = ""
if money >= 10000 or card:
    res = "택시를 타자"

print(res)
print("수고 하셨습니다.")
print('-'*30)

