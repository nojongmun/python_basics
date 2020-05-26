'''''
클래스명 : Sales
- item : str
- qty : int
- cost : int

+property, *.setter

+ *.__str__()  ==> 출력문 
+ getPrice()   ==> qty*cost(수량 * 단가)를 리턴 

--출력 
apple   1200원짜리 5개 구입하려면 6000원이 필요함  

'''''

class Sales:



    def getPrice(self):
        return self.qty*self.cost

    def __str__(self):
        return self.item+'   '+str(self.cost)+\
               '원짜리 '+str(self.qty)+'개 구입하려면 '+\
               str(self.getPrice())+'원이 필요함 '

if __name__ == '__main__':
    ss=Sales()
    ss.item='apple'
    ss.qty = 5
    ss.cost = 1200
    print(ss.__str__())





















