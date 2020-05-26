# 전치 연산 : 행렬 교환
import numpy as np

ar = np.array([[0,1,2], [3,4,5]])
print(ar)
print(ar.T)  # T 속성을 사용하여 교환
print('------------------------------------------')

# 배열의 크기 변형
a = np.arange(12)
print(a)
b= a.reshape(3,4)
print(b)
print('------------------------------------------')

print(a.reshape(4, -1))  # -1는 알아서 계산
print(a.reshape(-1, 6))
print(a.reshape(-1, 2))
print('------------------------------------------')

print(a.reshape(2,2,-1))
print("다차원배열 펼치기 : ", (a.reshape(2,2,-1)).flatten())
print("다차원배열 펼치기 : ", (a.reshape(2,2,-1)).ravel())