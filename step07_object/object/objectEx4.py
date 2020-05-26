from step07_object.object.employee import Employee
# 이름은 이순신이고 개발부에 근무하며 급여는 1500000원 입사성적은 85.75점입니다

if __name__ == '__main__':
    em = Employee()     # 객체생성 : 초기화 메서드(생성자, 초기자) 호출

    em.name = '이순신'
    em.dept = '개발부'
    em.pay = 1500000
    em.score = 85.75

    print(em.__str__()) # __str__() : 문자열 생성 메서드































