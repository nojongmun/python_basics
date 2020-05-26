''''' 
클래스 : 사용자가 만드는 자료형 
클래스 명 : Person
name : str
age : int
score : float

setPerson(name, age, score)
viewPerson
'''''


class Person:
    name = ''
    age = 0
    score = 0.0

    def setPerson(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def viewPerson(self):
        print('이름 : ', self.name)
        print('나이 : ', self.age)
        print('점수 : ', self.score)


# 클래스는 객체를 만들어서 사용
if __name__ == '__main__':
    ps = Person()   # 참조 변수명이 ps인 객체 생성 (기억공간 :name, age, score)
    # a = 10          # 변수명이 a인 변수 생성  (기억공간  : 10)
    ps.setPerson('호랑이', 23, 85.5)
    # 바운드 메서드 호출 : 묵시적으로 첫 인자를 인스턴스 객체로 선언,
    #       인스턴스 객체를 통해 클래스 메서드 호출
    #
    ps.viewPerson()

    ps1=Person()
    Person.setPerson(ps1, '호냥이', 15, 75.5)
    # unbound 메서드 호출 : 명시적으로 첫인자로 인스턴스 객체를 전달,
    #       클래스를 통해 메서드를 호출
    #       클래스에서 인스턴스 객체를 받아서 호출
    Person.viewPerson(ps1)

#     클래스의 오브젝트는 인스턴스



































