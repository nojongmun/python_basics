# 사다리꼴의 넓이 구하기
from step07_object.object.tra import Trapezoid

while True:
    print('*** 사다리꼴의 넓이 구하기 ***')

    base = int(input('밑변 : '))
    top = int(input('윗변 : '))
    height = int(input('높이 : '))


    # tar  클래스로 객체를 만들어서 넓이 구하기
    tz = Trapezoid()
    tz.setTrapezoid(base,top, height)

    # __str__() : 오버라이드된 출력 스트림
    print(tz.__str__())

    yn = input('한번더 계산 ? (y/n) : ')
    if (yn=='y') or (yn=="Y"):
        continue
    else:
        break

print('수고요...')

