# slicing
tag = '<a href="https://www.google.co.kr">구글 웹사이트</a>'
print(tag.__len__())
print(tag[9:33])

# copy
numbers=[1,2,3,4,5,6,7,8]
print(numbers)
print(numbers[:])

numbers2=numbers[:] # 기억 공간의 공유가 아닌 값의 복사를 통한 기억공간 생성
numbers.append(9)
print('numbers : ', numbers)
print('numbers2 : ', numbers2)
print('-----------------------')

print(numbers[:10:1]) # 0~9번째 기억공간을 1씩 지나가면서 출력

print(numbers[:10:2])
print(numbers[::2]) # 전체 영역에 대하여 2씩 지나가며 출력

print(numbers[9:0:-2]) # 역방향 순회
# print(numbers[8:0:-2])
print(numbers[:5:-2]) # 시작부터 5번째 다음까지 역방향으로 두칸씩 건너가면 출력






















