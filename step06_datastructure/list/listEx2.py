li=[]   # 요소가 없는 빈 리스트 생성
li=[1,2,3,4,5,6,7,8,9,10]

# 리스트 슬라이싱
lst1= li[1:5] # 슬라이싱할때의 값의 인덱스 값
print('lst1 : ', lst1)

lst2 = li[:5] # 0번 인덱스 부터 시작 5보다 작은 요소까지 [0:5]
print('lst2 : ', lst2)

lst3 = li[5:] # 5번째 요소부터 끝까지
print('lst3 : ', lst3)

del li[5]
print('li : ', li) # 5번재 요소 6제거

# 리스트 반복
lst_iter = lst1 * 5  # 지정한 횟수(5) 만큼 반복 된 값을 저장
print('lst_iter : ', lst_iter)

# 리스트 병합
lst_concat = lst2+lst3
print('lst_concat : ', lst_concat)

# list comprehension(LC)
# [출력표현식 for 요소 in 시퀀스데이터 [if 조건식]]
lst = [n**2 for n in range(10) if n%3==0 ]
# 0~9까지의 숫자중 3으로 나눈나머지가 0인 값에 대하여 제곱한 값에 대한 리스트
print('lst comprehension : ', lst)
# [print(n**2, end=' ') for n in range(10) if n%3==0 ]

# for n in range(10): # 27라인과 동일
#     if n%3 == 0:
#         print(n)

# 문자열 분해
parse = list('hello')
print('문자열 분해 : ', parse)

# 문자열 결합
print(' '.join(parse))
# 따옴표 안의 값을 연결자로 사용하여 리스트를 연결 ,
# 분해된 리스트를 하나로 묶기

x = [None]*20 # 값이 없는(None) 기억 공간 20칸을 가진 리스트 x 생성
print(x)
# None : 값이나 기억공간이 없는 상태를 표현 , 예약어, NULL, null






























