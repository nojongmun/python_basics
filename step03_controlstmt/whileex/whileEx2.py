'''''
[문제] 단을 입력 받아 구구단을 출력하세요 

단을 입력하세요 : 7
7 * 1 = 7
7 * 2 = 14
    :
7 * 9 = 63

'''''
# print('단을 입력하세요 : ')
# dan=input()

dan=int(input('단을 입력하세요 : '))
n=1

while n<=9:
    print(dan, ' * ', n, ' = ', dan*n)
    n+=1  # n= n+1





