import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
tips = sns.load_dataset('tips') # 팁 데이터세 로드

# print(tips)

# sns.relplot(x='total_bill', y='tip', data=tips) # 2차원 산점도

# hue 시맨틱 :  hue에 따라 점을 구분
# sns.relplot(x='total_bill', y='tip', hue='smoker', data=tips) # 2차원 산점도

# style 지정에 따라 마커의 모양이 달라짐
# sns.relplot(x='total_bill', y='tip', hue='smoker',style='smoker',data=tips) # 2차원 산점도
# sns.relplot(x='total_bill', y='tip', hue='smoker',style='time',data=tips) # 2차원 산점도
# sns.relplot(x='total_bill', y='tip', hue='smoker',style='day',data=tips) # 2차원 산점도

# 색상은 seaborn이 가지고 있는 기본 색상
# palette를 이용해서 지정할 수 있다.
# sns.relplot(x='total_bill', y='tip', hue='size',palette='ch:r=-.5, l=.75' ,data=tips) # 2차원 산점도

# 값에 따라 원의 크기가 달라 진다.
# sns.relplot(x='total_bill', y='tip', hue='smoker',size='tip',data=tips) # 2차원 산점도
# sns.relplot(x='total_bill', y='tip', hue='smoker',size='tip', sizes=(10,100),data=tips)  # 2차원 산점도

# kind = 그래프의 종류
# sns.relplot(x='total_bill', y='tip', hue='smoker',kind='line',data=tips)  # 2차원 산점도

# lineplot 그리기
df = pd.DataFrame(dict(time=np.arange(500),value=np.random.randn(500).cumsum()))

sns.relplot(x='time', y='value', kind='line', data=df)


plt.show()

