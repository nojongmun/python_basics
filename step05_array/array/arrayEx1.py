# 1차원 배열, 리스트
# 배열 : 동일한 자료형의 연속된 기억공간
# 리스트 : 서로 다른  자료형의 연속된 기억공간

num = [10, 20, 30, 40, 50]

print(type(num))

num[2] = 33
for i in num:   # 기억 공간의 순회
    print(i, end=' ')

print('\n------------------')
for i in range(0, num.__len__()): # 첨자(인덱스)를 활용한 출력
    print(num[i], end=' ')

print('\n------------------')
for i in range(num.__len__()-1, -1, -1):# 역순으로 출력
    print(num[i], end=' ')

# print(len(num))






















