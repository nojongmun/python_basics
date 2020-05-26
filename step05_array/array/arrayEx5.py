# 크기가  5인 정수형 배열을 만들고
# 배열에 데이터를 입력 받아서 출력하고 최대 , 최소값을 구하세요

# ar[0]의 값을 입력하세요 : 25
# ar[1]의 값을 입력하세요 : 25
# ar[2]의 값을 입력하세요 : 25
# ar[3]의 값을 입력하세요 : 2
# ar[4]의 값을 입력하세요 : 25

# 최대값 : 25
# 최소값 : 2
import array

ar=array.array('i')

for i in range(0,5):
    ar.append(int(input('ar[%d]의 값을 입력하세요 : ' % i)))

print(ar)

print('최대값 : ', max(ar))
print('최소값 : ', min(ar))
