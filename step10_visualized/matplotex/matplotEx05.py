import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set(xlim=[0,8], ylim=[0,40])

x = np.array([1,3,5,7])        # x축 값으로 사용
y = np.array([10,25,15,30])    # y축 값으로 사용

# x, y 값을 사용하여 점을 찍고 연결

# ax.plot(x,y)  #line2D,  꺽은 선 그래프

# ax.plot(x,y,marker='*' , color='darkgreen')
# ax.plot(x, y, marker='o', color='red', linewidth=1)
ax.scatter(x, y, marker='*', color='red')  # 분포도에서 많이 사용
# marker는 제한적인 특수 문자 사용 가능 : ^ , * , o, x

plt.show()
