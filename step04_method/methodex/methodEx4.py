def total(k, e, m):
    return k+e+m

def avg(total):
    return total/3

def grade(avg):
    avg=int(avg/10)  # avg/=10

    return {
        10 : 'A',
        9 : 'A',
        8: 'B',
        7: 'C',
        6: 'D',
    }.get(avg, 'F')
# result
def result(grade):
    # return '불합격' if grade=='F' else '합격'

    if grade == 'F':
        return '불합격'
    else:
        return '합격'

print('합계 : ', total(95, 85, 73))
print('평균 : %.2f점' % avg(total(95, 85, 73)))
print('학점 : ', grade(avg(total(95, 85, 73))))
print('결과 : ', result(grade(avg(total(95, 85, 73)))))


















