class User:
    _name = ''
    _k=0
    _e=0
    _m=0

    def setUser(self, name, k, e, m):
        self._name=name
        self._k=k
        self._e=e
        self._m=m

    def getTotal(self):
        return self._k + self._e + self._m

    def getUser(self):
        return '이름은 '+self._name + "이고 총점은 "+str(self.getTotal())+"점입니다\n"

# if __name__ == '__main__':
#     print('user.py')



