# 메서드 : method, 함수, function, procedure
# call by name : 이름만 있는 함수 ,  procedure

'''''
def 함수명(입력파라미터):
    문장1
    문장2...
    return 리턴값 
'''''

def view():     # 함수 정의
    print('hello')
    return      # 제어만 이동, 생략

def star():
    print('*****')

if __name__ == '__main__':  # 프로그램의 엔트리 포인트
    # 모듈은 import될때 실행이 되는데 이를 막기 위해 __name__ 이 __main__인지 검사
    # __name__ 이 __main__이면 쉘에서 실행할때이므로 동작을 하게 됨
    # import 된 경우는 실행되지 않음
    view()      # 함수 호출
    star()
    view()
    star()






















