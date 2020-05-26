class Trapezoid(object):
    __base = 0
    __top = 0
    __height = 0

    # self : 자기 클래스의 객체 인식, self 대신 다른 이름을 적어도 됨
    def setTrapezoid(self, base, top, height):
        self.__base = base
        self.__top = top
        self.__height = height

    def cal(self):
        return (self.__base+self.__top)*self.__height / 2

    # 오버라이드 되었음 (반드시 문자열로 리턴 ;  자바의 toString() 과 같음)
    def __str__(self):
        return "넓이:"+str(self.cal())