import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set_xlim([-3.5, 3.5])
ax.set_ylim([-1.2, 1.2])
ax.set_xticks([-np.pi,  -np.pi/2, 0, np.pi/2, np.pi])   # x축에 표시할 내용
ax.set_xticklabels(['$-\pi$','$-\pi/2$','0','$\pi/2$','$\pi$'])   # x축 라벨

# 틱의 위치 변경
# ax.xaxis.set_ticks_position('bottom')  # 기본
# ax.xaxis.set_ticks_position('top')
# ax.yaxis.set_ticks_position('left')    # 기본
# ax.yaxis.set_ticks_position('right')

# 사인, 코사인 함수
# x = np.linspace(-np.pi,  np.pi, 숫자(갯수))
x = np.linspace(-np.pi,  np.pi)
siny = np.sin(x)
cosy = np.cos(x)


ax.plot(x, siny, color='blue', linewidth=2, marker='^')
ax.plot(x, cosy, color='red', linewidth=2)

plt.show()
