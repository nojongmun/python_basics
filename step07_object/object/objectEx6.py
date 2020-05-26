class MemberPhone(object):
    #  __name=""   # __ 묵시적으로 private 선언
    #  __phone=""
    #
    # def input_mp(self):
    #     self.__name = input('이름을 입력하세요 : ')
    #     self.__phone = input('전화를 입력하세요 : ')


    def input_mp(self):
        self.name = input('이름 : ')
        self.phone = input('전화 : ')

    def output_mp(self):
        print(self.__name+'고객님의 전화번호는 '+self.__phone+'입니다.')

if __name__ == '__main__':
    mp = MemberPhone()
    mp.input_mp()

    mp.output_mp()