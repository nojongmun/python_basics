def show1(a, b, c, d):
    print(a, b, c, d)

def show2(k, e, m):
    return (k+e+m)/3

def show3(k, e, m):
    avg = (k+e+m)/3
    if avg>=60:
        return '합격'
    else:
        return '불합격'




show1(10, 'A', 100.4, True)
a=show2(95, 85, 73)
print('평균 : %.2f' % show2(95, 85, 73))
print(a)
print('결과 : ', show3(95,85,73))


















