# python ArrayEx3 abc 12345 가나다 1234

import sys

print('argv의 길이 : ', len(sys.argv))
print('argv[0] : ', sys.argv[0])

for i in range(1, len(sys.argv)):
    # print(sys.argv[i])
    print('argv[', i, '] : ', sys.argv[i])
    print('argv[', i, ']의 길이 : ', sys.argv[i].__len__())
























