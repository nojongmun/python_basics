hap = 0
odd=0
even=0

for i in range(101):
    hap += i
    if i%2 == 1:
        odd += i
    else :
        even += i

print('1-100까지의 합 : ', hap)
print('1-100까지의 홀수합 : ', odd)
print('1-100까지의 짝수합 : ', even)


print(sum(range(101)))




















