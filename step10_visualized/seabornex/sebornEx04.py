# passengers 데이터 셋
# 히트맵
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
flights = flights.pivot('month','year','passengers')
# print(flight)

# sns.heatmap(flights)

# annot : 각 셀에 정수로 해당하는 값을 주석으로 표시
# sns.heatmap(flights, annot=True)

# fmt : 셀에 표시할  annotdate의 서식 지정
# sns.heatmap(flights, annot=True, fmt='d')

# sns.heatmap(flights, annot=True, fmt='d', linewidths=2, linecolor='yellow')


# sns.heatmap(flights, annot=True, fmt='d', cmap='CMRmap_r') # 오류에서 나오는 메세지에서 정당히 골라 쓸수 있다.
# sns.heatmap(flights, annot=True, fmt='d', cmap='YlOrBr')

# cbar : 컬러 바
sns.heatmap(flights, annot=True, fmt='d', cmap='YlOrBr', cbar=False)

plt.show()

