# 시리즈 연산 : 연산은 시리즈의 값에만 적용, 인덱스는 불변

import pandas as pd
import step09_da.pandas.pandasEx01 as ex01

div = ex01.city / 1000000
print(div)
print('-'*50)

# 시리즈 인덱싱
print(ex01.city[1], ex01.city['대전'])
print(ex01.city[3], ex01.city['부산'])
print('-'*50)

# 배열 인덱싱을 사용할 경우 순서 변경 가능
print(ex01.city[[1, 3, 0]])
print(ex01.city[['대전', '서울', '부산']])
print('-'*50)

# 문자열 라벨을 이용한 슬라이싱
print(ex01.city[1:3])            # 3 은 포함 하지 않음
print(ex01.city['서울':'대구'])  # 대구 포함 됨 (inclusive)
print('-'*50)

a = pd.Series(range(3), index=['a', 'b', '다'])
print(a)
print('-'*50)
print(a['a'])   # 0
print(a.a)      # 0
print(a.b)      # 1
print(a.다)     # 2 , 요즘은 한글 사용도 가능
print('-'*50)



