class Member(object):
    pass
    # __name = ""   # 생략가능
    # __age = 0
    # __tall = 0.0

    # @property
    # def name(self):     # getter
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name=value
    #
    # @property
    # def age(self):     # getter
    #     return self.__age
    #
    # @age.setter
    # def age(self, value):
    #     self.__age=value
    #
    # @property
    # def tall(self):     # getter
    #     return self.__tall
    #
    # @tall.setter
    # def tall(self, value):
    #     self.__tall=value
    #


if __name__ == '__main__':
    ob = Member()
    ob.name ='호랑이'   # @property 생략해도 동작 잘됨
    ob.age=500
    ob.tall=305.5

    print('이름 : ', ob.name) # @name.setter 생략해도 동작 잘됨
    print('나이 : ', ob.age)
    print('신장 : ', ob.tall)

































