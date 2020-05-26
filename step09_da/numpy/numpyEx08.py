# numpy가 제공하는 배열 생성 명령(함수)
import numpy as np


# zeros : 크기가 정해진  모든 값이 0인 배열 생성(매개변수는 배열의 크기)
z_ar = np.zeros(5)
print('제로 배열', z_ar)
print(z_ar.dtype)
print('---------------------------------------')
z_2dar = np.zeros((2,3))
print('제로 2d배열 ')
print(z_2dar)
print(z_2dar.dtype)
print('---------------------------------------')
z_2dar1 = np.zeros((2,3),dtype='f')
print(z_2dar1)
print(z_2dar1.dtype)
print('---------------------------------------')
o_ar = np.ones((2,3,4))
print(o_ar)
print('---------------------------------------')
# ones_like, zeros_like 배열의 크기를 지정하지 않고 다른 배열의 크기를 차용
ol_ar = np.ones_like(z_2dar, dtype='f')
print('ones like\n', ol_ar)
zl_ar = np.zeros_like(o_ar, dtype='f')
print('zeros like\n', zl_ar)
print('---------------------------------------')
e_ar = np.empty((4,3)) # empty는 배열만 생성하고 초기화를 하지 않음
print(e_ar)
print(e_ar.dtype)
print('---------------------------------------')
ar =  np.arange(10)
print(ar)

ar1 = np.arange(3,21,3) # arange(시작, 끝, 간격)
print(ar1)

ls = np.linspace(0,100,5) #
# linspace(시작, 끝, 갯수)
print(ls)



