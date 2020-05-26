import numpy as np
import matplotlib.pyplot as plt
# settings 에서 seaborn 추가
# https://seaborn.pydata.org/ 참조
import seaborn as sns

# step09_da > numpyEx07.py 정보 가져오기
x = np.array([18, 5, 10, 23, 19, -8, 10, 0, 0, 5, 2, 15, 8,
               2, 5, 4, 15, -1, 4, -7, -24, 7, 9, -6, 23, -13,
               1, 0, 16, 15, 2, 4, -7, -18, -2, 2, 13, 13, -2,
              -2, -9, -13, -16, 20, -4, -3, -11, 8, -15, -1, -7, 4,
              -4, -10, 0, 5, 1, 4, -5, -2, -5, -2, -7, -16, 2,
              -3, -15, 5, -8, 1, 8, 2, 12, -11, 5, -5, -7, -4], )

# hist  : 히스토그램
# bins : 구간의 경계값 리스트
# n : 각 구간에 포함된 값의 개수 또는 빈도 리스트
# patches : 각 구간의 값을 그리는 matplotlib patch 객체 리스트
n, bins, patches = plt.hist(x, bins=20)
# print('n : ' , n)
# print('bins : ', bins)
# print('patches : ', patches)

sns.distplot(x, rug=True)

plt.show()

