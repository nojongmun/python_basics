import  pandas as pd
import step09_da.pandas.pandasEx01 as ex01

# 주로 검색 용도로 사용
print('서울' in ex01.city)  # True
print('수원' in ex01.city)  # False
print('-'*50)

for k, v in ex01.city.items():
    print('%s = %d' %(k, v))
print('-'*50,"\n")
print('-- 딕셔너리 객체에서 시리즈 생성 --')
# 2015년도 도시별 인구수
city = pd.Series({'서울':10022181, '대전':1518775, '대구':2487829, '부산':3513777})
print(city)
print('-'*50,"\n")
# 딕셔너리 처럼 시리즈도 순서가 없음
# 순서를 지정하고 싶은 경우 index를 리스트로 지정하면 된다.
city = pd.Series({'서울':10022181, '대전':1518775, '대구':2487829, '부산':3513777},
                 index=['서울','대구','대전','부산'])
print(city)
print('-'*50,"\n")

print('--- 인덱스 기반 연산 ---')
dist = ex01.city - city
print('도시별 인구 증감 \n' ,  dist);
print('-'*50,"\n")

print('--- 인덱스 기반 연산2 ---')
dist = ex01.city.values   - city.values
print('도시별 인구 증감 \n' ,  dist);
city = pd.Series({'서울':10022181, '대전':1518775, '대구':2487829, '부산':3513777, '인천':2925815}
                 ,index=['서울','대구','대전','부산','인천'])
print(city)
print('-'*50,"\n")

dist2 = ex01.city - city;
print(dist2)             # 인천은 NaN(Not a Number) , dtype이 변경됨
print('-'*50,"\n")
print(dist2.notnull())  # 데이터가 없으면 False
print('-'*50,"\n")

print(dist2[dist2.notnull()]) # 데이터가 없으면 출력하지 말아라
print('-'*50,"\n")
ratio = (ex01.city - city) / city * 100
print(ratio[ratio.notnull()])
print('-'*50,"\n")

print('--- 인덱싱을 이용한 데이터 갱신 추가 삭제 ---')
ratio['부산'] = 1.23
print(ratio)

ratio['수원'] = 2.03
print(ratio)

del ratio['서울']
print(ratio)




