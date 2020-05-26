import matplotlib.pyplot as plt

fig=plt.figure()
ax = fig.add_subplot(1, 1, 1)
# 창을 가로 1칸, 세로 1칸으로 분할 하고 그 중 첫번째 칸에
# ax 라는 이름의 axes(액시스)를 생성

# axes는 figure 내에서 축을 가지는 하나의 좌표 평면과 같은 개념
# add_axes() 함수를 사용하여 figure 클래스에 axes를 생성 할 수 있습니다.
# add_subplot()을 사용하여 그림을 그려도 됨 (축 그리기)

plt.show()

