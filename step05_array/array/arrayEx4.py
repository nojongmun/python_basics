# 숫자 3개를 입력 받아 최대 최소값 구하기
# python arrayEx4 10 15 23

# 최대값 : 23
# 최소값 : 10

import sys
import array

ar = array.array('i')  # array 초기화 , 'i' : 타입 코드 , signed int

# print(type(ar))
for i in range(1, len(sys.argv)):
    ar.append(int(sys.argv[i]))

# print(ar)
print('최대값 : ', max(ar))
print('최소값 : ', min(ar))

# -------------------------------------------

ar = []  # 리스트 초기화

print('ar type : ', type(ar))
for i in range(1, len(sys.argv)):
    ar.append(int(sys.argv[i]))

# print(ar)
print('최대값 : ', max(ar))
print('최소값 : ', min(ar))
























