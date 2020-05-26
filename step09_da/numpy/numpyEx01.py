# numpy : 수치해석용 파이썬 패키지, 넘파이
# 다차원 배열 자료구조인 ndarray(핸디어레이) 클래스 지원
# 벡터, 행렬을 사용하는 선형대수 계산에 사용
# 백터화 연산 지원

# import numpy
# # 1차원 배열
# ar = numpy.array

import numpy as np
# 1차원 배열
# numpy의 array()에 리스트(or 시퀀스값)을 넣으면 numpy 배열로 변화
ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)
print(type(ar))
print('-'*60)

# a1 = list([0,1,2,3,4,5,6,7,8,])
# print(a1)
# print(type(a1))

# 백터화 연산  ---------------------
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1. for문으로 연산
answer = [];
for d in data:
    answer.append(2*d)
print('data의 배수  : ', answer)
print('data의 n회 출력  : ', data*2)
print('data의 n회 출력  : ', answer*2)

# 2. 백터화 연산(numpy에서 제공)
x = np.array(data)
print('백터화 연산 : ', x*2)

# 백터화 연산은 수치연산, 논리연산, 관계연산 등의 모든 수학 연산에 적용 가능
print('-' * 60)

# 3. 백터화 연산
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(2*a+b)
print('a는 2인가 ? ', a == 2)
print('b는 10 보다 큰가 ? ', b > 10)
print( (a == 2) & (b > 10))  # and 연산
print( (a == 2) | (b > 10))  # or 연산



