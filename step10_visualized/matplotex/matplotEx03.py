import matplotlib.pyplot as plt

# 창 분할
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
# 전체 창을 가로2칸 세로 1칸 분할
# 첫번째 칸에 ax1, 두번째 칸에 ax2를 생성

plt.show()