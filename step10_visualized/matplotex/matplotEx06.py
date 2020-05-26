import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# ax.set(xlim=[0, 3])
# ax.set_xlim(left=0, right=3)

# ax.set(ylim=[-2, 1])
# ax.set_ylim(bottom=-2, top=1)

ax.set_xlim([0,30])
ax.set_ylim([200,0])

ax.set_xlabel('Temperature($^{\circ}$C)')  # latext 문법에 따른 것
ax.set_ylabel('Depth(m)')  # latext 문법에 따른 것

plt.show()
