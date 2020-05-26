# 배열 인덱싱 ;  팬시 인덱싱  fancy indexing
# 배열 인덱싱의 종류 : 정수인덱싱, 불리언 인덱싱

import numpy as np
a = np.array([0,1,2,3,4,5,6,7,8,9])
idx = np.array([True,False,False,False,True,
                True,False,True,False,True])
print(a[idx])
print(a%2==0)
print(a[a%2==0])   # 불리언 인덱싱  # 짝수 index 값만 리턴
print('------------------------------')
a = np.array([11,22,33,44,55,66,77,88,99])
idx = np.array([0,2,4,6,8]) # <== 인덱스 배열의 크기는 제한 없다.
# 인덱스 배열의 원소 각각 ndarray 객체를 가리키는 인덱스 정수여야 함
# ndarray 객체의 범위를 벗어나는 index가 오면 에러

print(a[idx]) # 정수 배열 인덱싱
print('------------------------------')

# 다차원 배열에서의 배열 인덱싱
x = np.array([[0,1,2,3,4],
               [5,6,7,8,9],
               [10,11,12,13,14]])
print(x)
print(x[:, [True,False,False,True,False]])  # 행단위로 인덱스 처리
print('------------------------------')
# 문제
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# 1. 3의 배수를 배열 인덱싱 하세요
# 2. 4로 나누면 1이 남는 수를 인덱싱 하세요
# 3. 3으로 나누면 나누어 떨어지고 4로 나누면 1이 남는 수를 찾으세요
print(x[x%3==0])
print(x[x%4==1])
print(x[(x%3==0)&(x%4==1)])

