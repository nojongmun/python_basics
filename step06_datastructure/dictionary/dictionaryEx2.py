# 딕셔너리 생성
# {}를 사용하여 생성 가능
# dict() 생성자를 사용할수 있음

# 1. 키 밸루 쌍을 갖는 튜플 리스트로 부터 dict 생성
person = [('민들래', 30), ('개나리', 35), ('진달래',25)]
mydict = dict(person)

print(type(mydict))

age = mydict['개나리']
print(age)

# 2. key=value 파라미터를 이용하여 dict 생성
score = dict(a=80, b=90, c=85)
print(score['b'])

# ----------------------------------------------
# 추가, 삭제, 수정, 읽기

score= {'진달래':75, '개나리':85, '민들래':93}

score['진달래'] = 83  # 수정
score['뽀로로'] = 73  # 추가
del score['개나리']

print(score)























