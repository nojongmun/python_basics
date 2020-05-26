# 다차원 데이터 분포 : 순서가 정해져 있는 여러개의 1차원 데이터가 있는 구조
# 산점도 :  2 차원 데이터이고 각 데이터가 연속적인 실수값을 가지는 경우 사용 (scatter plot)
# jointplot : 산점도 + 히스토그램

import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
# print(iris.head())
print(iris.tail())

# sns.jointplot(x='sepal_length', y='sepal_width', data=iris) # 기본 조인트 플롯

# 인수가 변경되는 경우 히스토그램을 커널밀도 형태로 표현 가능
# sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='kde')

# 3차원 이상의 데이터는 pairplot을 사용
# 그리도 형태, 히스토그램을 조합하여 표현
sns.pairplot(iris, hue='species', markers=['o','^','s'])

plt.show()

