import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

tips = sns.load_dataset('tips')
print(tips)

# 바이올린 플롯
# sns.violinplot(x=tips['total_bill'])

# 범주형 변수로 그룹화된 수직 바이올린 플롯
# sns.violinplot(x='day', y='total_bill', data=tips)

# 중첩화된 범주형 변수로 그룹화된 수직 바이올린 플롯
# sns.violinplot(x='day', y='total_bill', hue='smoker',  data=tips)


# order=['Dinner', 'Lunch'] 순서 지정
# sns.violinplot(x='time', y='total_bill', data=tips)
# sns.violinplot(x='time', y='total_bill', data=tips, order=['Dinner', 'Lunch'])

# 요일별, 성별별 전체 지불금액 : 각 값의 수로 바이올린 플롯의 너비 결정
# sns.violinplot(x='day',y='total_bill', hue='sex', data=tips)
# sns.violinplot(x='day',y='total_bill', hue='sex', data=tips, split=True)
sns.violinplot(x='day',y='total_bill', hue='sex', data=tips, split=True, scale='count')



plt.show()

