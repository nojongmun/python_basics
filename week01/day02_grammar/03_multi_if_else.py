# 중첩 if문 : if-else 문이 여러개 나올때

# if 조건식1:
#       조건식1이 참일때 실행할 문장
# elif 조건식2:
#       조건식1이 거짓이면서 조건식2  참일때 실행할 문장
# elif 조건식3:
#       조건식1,2이 거짓이면서 조건식3  참일때 실행할 문장
# else:
#       조건식1,2,3 모두 거짓일때 실행할 문장.

# k1의 점수가 90이상이면 A, 80이상이면 B, 70이상이면 C, 나머지 F
k1 = 95
res = ""
if  k1 >= 90:
    res ="A"
elif k1 >= 80:
    res = "B"
elif k1 >= 70:
    res = "C"
else:
    res = "F"

print("결과 : " + res)

# menu가 1이면 카페모카 3500, 2이면 카페라떼 4000, 3이면 아메리카노 3000,
# 4이면 과일쥬스 3500이다. 친구와 2잔을 10000내고 먹었다.
# 잔돈은 얼마인가? (부가세 10% 포함)

menu = 4
if menu == 1:
    str1= "카페모카"
    dan = 3500;
    su = 2;
    total = dan * su;
    vat = (int)(total * 0.1);
    input = 10000;
    output = input - (total + vat);
    print(output)
elif menu == 2:
    str1 = "카페라떼"
    dan = 4000;
    su = 2;
    total = dan * su;
    vat = (int)(total * 0.1);
    input = 10000;
    output = input - (total + vat);
    print(output)
elif menu == 3:
    str1 = "아메리카노"
    dan = 3000;
    su = 2;
    total = dan * su;
    vat = (int)(total * 0.1);
    input = 10000;
    output = input - (total + vat);
    print(output)
elif menu == 4:
    str1 = "과일쥬스"
    dan = 3500;
    su = 2;
    total = dan * su;
    vat = (int)(total * 0.1);
    input = 10000;
    output = input - (total + vat);
    print(output)

# 리펙토링 ( 코드를 간결하게 , 중복제거)

menu = 2
if menu == 1:
    str1= "카페모카"
    dan = 3500;
    su = 2;
elif menu == 2:
    str1 = "카페라떼"
    dan = 4000;
    su = 2;
elif menu == 3:
    str1 = "아메리카노"
    dan = 3000;
    su = 2;
elif menu == 4:
    str1 = "과일쥬스"
    dan = 3500;
    su = 2;

total = dan * su;
vat = (int)(total * 0.1);
input = 10000;
output = input - (total + vat);
print(output)

