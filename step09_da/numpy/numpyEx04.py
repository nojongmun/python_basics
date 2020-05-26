# ndim 속성 : 배열의 차원 리턴,  shape 속성 : 배열의 크기 값 리턴

import numpy as np
# 임포트르 해서 numpyEx03일 실행 된다. 방지 하기 위해서 numpyEx03에 main을 만들어주면 됨
import step09_da.numpy.numpyEx03 as ex03

# 1차원 배열의 속성
a = np.array([1,2,3])
print(a.ndim)     # 1 => 1 차원
print(a.shape)    #(3,) => 결과를 튜플로

# 2차원 배열의 속성
b = np.array([[1,2,3],[4,5,6]])
print(b.ndim)
print(b.shape)

# 3차원 배열의 속성
print(ex03.d.ndim)
print(ex03.d.shape)
