# 데이터 프레임
# 시리즈 : 1차원 백터 데이터에 행방향 인덱스를 붙인 것
# 데이터프레임 : 2차원 행렬데이터에 인덱스를 붙인 것

import pandas as pd
import numpy as np
from pandas import DataFrame

print('--- 데이터 프레임 생성 ---')
# 1. 하나의 열이 되는 데이터를 리스트나 1차원 배열로 준비
# 2. 이 각각의 열에 대한 이름을 키로 가지는 딕셔너리 만들기
# 3. 이 데이터를 DataFrame 생성자에 넣으면서
# 4. 열 방향 인덱스는 columns 인수를 사용하고, 행방향 인덱스는 index 인수로 지정

df = DataFrame(['뽀로로', '패티', '크롱', '루피', '에디'])
print(df)
print('-'*70, '\n')
print(df[0])
print('-'*70, '\n')

df = DataFrame({'name': ['뽀로로', '패티', '크롱', '루피', '에디']})
print(df)
print('-'*70, '\n')

df = DataFrame({'name': ['뽀로로','패티','크롱','루피','에디']},
               index=['no_1','no_2','no_3','no_4','no_5'])
print(df)
print('-'*70, '\n')

# 데이터 추가
df = DataFrame({'name': ['뽀로로','패티','크롱','루피','에디'],
               'id':['pororo','paty','cron','rupy','edi']},
               index=['no_1','no_2','no_3','no_4','no_5'])
print(df)
print('-'*70, '\n')

# 데이터 추가
df = DataFrame({'name': ['뽀로로','패티','크롱','루피','에디'],
               'id':['pororo','paty','cron','rupy','edi'],
               'addr': ['신논현','역삼','정릉','안암','서초']},
               index=['no_1','no_2','no_3','no_4','no_5'])
print(df)
print('-'*70, '\n')

print('--- 데이터 프레임 생성 2 ---')

data = {
        "2015": [9904312, 3448737, 2890451, 2466052],
        "2010": [9631482, 3393191, 2632035, 2431774],
        "2005": [9762546, 3512547, 2517680, 2456016],
        "2000": [9853972, 3655437, 2466338, 2473990],
        "지역": ["수도권", "경상권", "수도권", "경상권"],
        "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]}

columns = ['지역','2015','2010','2005','2000','2010-2015 증가율']
index = ['서울','부산','인천','대구']

df = pd.DataFrame(data, index=index,columns=columns);
# df = pd.DataFrame(data, index,columns); 순서대로 넣기 때문에 상관없음
print(df)
print('-'*70, '\n')

print(df.values)
print('-'*70, '\n')

print(df.columns)
print('-'*70, '\n')

print(df.index)
print('-'*70, '\n')

df.index.name ='도시'
df.columns.name = '특성'
print(df)
print('-'*70, '\n')

print('---- 데이터 프레임 인덱싱 ----')
print(df['지역'])
print('-'*70, '\n')

print(df[['2010', '2015']])
print('-'*70, '\n')

print(type(df))         # 전체는 데이터 프레임
print('-'*70, '\n')

print(type(df['2010'])) # 일부는 시리즈
print('-'*70, '\n')

# print(df[0]) # 인텍스 이름이 지정된 경우 정수 인덱스 사용하면 에러

print('----- 열 데이터 추가 -----')
df['2005-2015 증가율'] = ((df['2015']-df['2005']) / df['2005'] * 100).round(2)
print(df)
print('-'*70, '\n')

# 데이터 프레임에서 행 인덱싱을 하는 경우 항상 슬라이싱을 처리해야 됨
print('----- 데이터 프래임 행 인덱싱 -----')
print(df[:1])
print('-'*70, '\n')

print(df[-1:])
print('-'*70, '\n')

print(df['서울':'인천'])
print('-'*70, '\n')

print('----- 개별 데이터 인덱싱 -----')
print(df['2015']['서울'])
print('-'*70, '\n')

#  print(df['서울']['2015'])  오류


























