# 2차원 배열
import numpy as np


# 2x3 행렬
c = np.array([[0, 1, 2], [3, 4, 5]])
print(' 2x3 행렬 __\n', c)
print(type(c))  # <class 'numpy.ndarray'>
print('-'*60)

# 2차원 배열의 행과 열의 개수 구하기
print('행의 개수 : ', len(c))
print('열의 개수 : ', len(c[1]))
print('-'*60)

# 문제 : numpy를 사용하여 다음과 같은 행렬을 만드시오
# 10 20 30 40
# 50 60 70 80
# 결과
# 2 x 4 행렬[0] : [10 20 30 40 ]
# 2 x 4 행렬[1] : [50 60 70 80 ]
# 내가 푼거
# x = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
# num = 0
# for i in x:
#     print('2 x 4 행렬 [', num, '] : ', i)
#     num = num + 1

#  강사님이 풀어준 거 
x = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print('2*4 행렬[0] : ', x[0])
print('2*4 행렬[1] : ', x[1])