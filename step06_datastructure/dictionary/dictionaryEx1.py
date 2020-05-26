# 딕셔너리 : 키와 값의 쌍 , 인덱싱 불가 , 키를 통해 값을 검색 (해시 테이블 구조 )
# 형식 : {key1:value1, key2:value2,...}
# 딕셔너리는 dict 클래스로 구현
# 딕셔너리의 키는 값을 변경할수 없는 이뮤터블 타입이어야 함
#           값 뮤터블, 이뮤터블을 사용할수 있음
# ==>딕셔너리의 키는 tuple을 사용할수 있으나 list는 사용할수 없음

# 문법 : 딕셔너리변수명={키1:값1, 키2:값2,...}
#        요소가 없는 경우 딕셔너리변수명={}
# 검색에는 딕셔너리변수명[키] 와 같이 키를 인덱스 처럼 사용

dic={101:'둘리', 201:'도우너', 301:'마이콜', 401:'또치'}

print('key : ', 101, ' vlaue : ', dic[101])
print('key : ', 201, ' vlaue : ', dic[201])
print('key : ', 301, ' vlaue : ', dic[301])
print('key : ', 401, ' vlaue : ', dic[401])


























