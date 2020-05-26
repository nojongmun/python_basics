import matplotlib.pyplot as plt
import seaborn as sns

# boxplot
# tips = sns.load_dataset('tips')
#
# sns.set_style('whitegrid')  # 안 나옴 (boxplot 를 해야 나모)
# plt.figure(figsize=(8,8))   # 안 나옴 (boxplot 를 해야 나모)
#
# sns.boxplot(x=tips['total_bill'],color='skyblue')  # 가로 형태
# # sns.boxplot(y=tips['total_bill'],color='skyblue')  # 세로 형태
#
# plt.show()

# catplot
titanic = sns.load_dataset('titanic')
# print(titanic)

# 나이에 따라서 성별, 기항지, 객실 등급에 따라 분류
# 가장 기본적인 형태
# sns.catplot(x='age', y='embark_town', hue='sex', row='class', data=titanic[titanic.embark_town.notnull()])

# kind='violin'  바이올린 플롯 형태
# sns.catplot(x='age', y='embark_town', hue='sex', row='class', data=titanic[titanic.embark_town.notnull()], kind='violin')

# palette='Set3' 색상 변경
sns.catplot(x='age', y='embark_town', hue='sex', row='class', data=titanic[titanic.embark_town.notnull()], kind='violin', palette='Set3')

plt.show()

