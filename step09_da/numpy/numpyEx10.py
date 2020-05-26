# 배열 연결 : hstack, vstack, dstack, stack, ...
import numpy as np
from numpy.core._multiarray_umath import ndarray

a1 = np.ones((2,3))
a2 = np.zeros((2,2))
print(a1)
print(a2)
print("--------------------------------------")

# print(a2)
# hstack : 행의 수가 같은 배열들을 연결 하여 하나의 배열로 생성
hs = np.hstack([a1,a2])
print('hstack\n', hs)
print("--------------------------------------")

# vstack : 열의 수가 같은 배열들을 연결 하여 하나의 배열로 생성
b1 = np.ones((2,3))
b2 = np.zeros((3,3))
vs = np.vstack([b1, b2, b1])
print('vstack\n', vs)
print("--------------------------------------")

# dstack : 배열을 깊이의 방향으로 붙이기
c1 = np.ones((3,4))
c2 = np.zeros((3,4))
ds = np.dstack([c1,c2])
print(ds)
print(len(ds), len(ds[0]), len(ds[0][0]))
print("--------------------------------------")

# stack : 사용자 지정 방향으로 붙이기
s1 = np.stack([c1, c2])
s2 = np.stack([c1, c2], axis=0)
s3 = np.stack([c1, c2], axis=1)
print('s1\n', s1)
print('s2\n', s2)
print('s3\n', s3)
print("--------------------------------------")

# tile : 동일한 배열을 반복하여 연결
ti = np.array([[0,1,2],[3,4,5]])
print('ti\n',ti)
print('tile1\n', np.tile(ti,5))
print('tile2\n', np.tile(ti,(3,2)))
print("--------------------------------------")

# 문제
# array([[  0.,   0.,   0.,   1.,   1. ],
#        [  0.,   0.,   0.,   1.,   1. ],
#        [  0.,   0.,   0.,   1.,   1. ],
#        [ 10.,  20.,  30.,  40.,  50. ],
#        [ 60.,  70.,  80.,  90., 100. ],
#        [110., 120., 130., 140., 150. ]]

# ones, zeros, range, hstack, vstack

x1 = np.zeros([3,3])
x2 = np.ones([3,2])
x_hs = np.hstack([x1,x2])

y1 = np.arange(10,160,10)
y2 = y1.reshape(3,5)   # x4 = x3.reshape(3,-1)'
y_vs = np.vstack([x_hs, y2])

print(y_vs)

































