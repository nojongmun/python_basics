import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set_xlim([-1, 1])
ax.set_ylim([-1.2, 1.2])
ax.set_xticks([-np.pi,  -np.pi/2, 0, np.pi/2, np.pi])   # x축에 표시할 내용
ax.set_xticklabels(['$-\pi$','$-\pi/2$','0','$\pi/2$','$\pi$'])   # x축 라벨

#  강제로 맞추기 1
# ax.spines['bottom'].set_position(('outward',-133))  # 안쪽으로 이동
# ax.spines['left'].set_position(('outward',-178))      # 바깥쪽으로 이동


# 문제의 정답
# ax.spines['bottom'].set_position(('data', 0))  # bottom을 y축, 0.5 위치로 이동
# ax.spines['left'].set_position(('data', 0))  # left을 y축, 1위치로 이동

# axes : 비율에 따라 이동 ( 아래쪽, 왼쪽 : 0  위쪽, 오른쪽 : 1)
# 문제의 정답
ax.spines['bottom'].set_position(('axes', 0.50))   # bottom의 위치를 아래ㅉ고으로 부터 50% 위치로 이동
ax.spines['left'].set_position(('axes', 0.50))     # left를 왼쪽으로 부터 50% 위치로 이동


# set_color : 축의 색 변경
ax.spines['bottom'].set_color('red')
ax.spines['left'].set_color('blue')
ax.spines['top'].set_color('none')    # none : 투명
ax.spines['right'].set_color('none')


# 사인, 코사인 함수
# x = np.linspace(-np.pi,  np.pi, 숫자(갯수))
x = np.linspace(-np.pi,  np.pi)
siny = np.sin(x)
cosy = np.cos(x)


ax.plot(x, siny, color='blue', linewidth=2)
ax.plot(x, cosy, color='red', linewidth=2)

plt.show()
