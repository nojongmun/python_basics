class Employee:
    __name=''   # __   : 접근 지정자
    __dept=''
    __pay=0
    __score=0.0

    @property
    def name(self):
        return self.__name
    @property
    def dept(self):
        return self.__dept
    @property
    def pay(self):
        return self.__pay
    @property
    def score(self):
        return self.__score
    @name.setter
    def name(self, value):
        self.__name=value
    @dept.setter
    def dept(self, value):
        self.__dept=value
    @pay.setter
    def pay(self, value):
        self.__pay=value
    @score.setter
    def score(self, value):
        self.__score=value



    def __str__(self):
        return '이름은 '+self.__name+'이고 '+self.__dept+\
               '에 근무하며 급여는 '+str(self.__pay)+'원 입사성적은 '+\
               str(self.__score)+'점입니다\n'