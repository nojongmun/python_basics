import matplotlib.pyplot as plt

fig = plt.figure()
ax=fig.add_subplot(1, 1, 1)

# ax.set_xlim([0., 10.])  # x축에 대해서 0-1까지 표현
# ax.set_ylim([-0.5, 2.5])  # x축에 대해서 0-1까지 표현
# ax.set_title('matplotEx04', size=15)  # 기본에서는 한글 깨짐
# ax.set_xlabel('x-axis', size=10)      # 축이름
# ax.set_ylabel('y-axis', size=10)

ax.set(xlim=[0, 1], ylim=[-0.5, 2.5], title='matplotEx04', xlabel='x-axis', ylabel='y-axis')  # 이 경우 사이즈 지정 못함

plt.show()