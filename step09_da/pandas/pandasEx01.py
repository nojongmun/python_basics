# 데이터 시계열 테이터(series)나 테이블(table)로 구성되어 있는데 판다스에서는
# 이런 데이터를 다룰 수 있는 Series, DataFrame 클래스를 제공

# 시리즈 클래스 : numpy의 1차원 데이터와 비슷하지만
# 데이터의 의미를 표시하는 index 를 붙일 수 있고,
# 데이터 자체는 value 라고 함
# 시리즈 => value + index

import pandas as pd

# 시리즈 생성
# 2017년 도시별 인구 데이터
city = pd.Series([9857426, 1502227, 2475231, 3470653],
                 index=['서울', '대전', '대구', '부산'])    # Series() => 생성자 , index 는 생략 가능


# 서울, 대전 ... 등을 인덱스 값이라고 함. 또는 인덱스 라벨이라고 함
# 인덱스 라벨은 날짜, 시간, 정수, 문자열등을 사용 할 수 있음.

# pandosEx02.py 때문에 넣어줌
if __name__ == '__main__':

    print(city)            # 데이터 처리는 항상 열 단위 처리가 기본이다.
    print(type(city))
    print('-' *50);
    # print(pd.Series(range(10,14)))  # range() 사용가능

    print(city.index)    # 인덱스 출력
    print(city.values)   # value 출력
    print('-' *50);

    city.name='도시별 인구수'
    print(city)
    print('-' *50);





