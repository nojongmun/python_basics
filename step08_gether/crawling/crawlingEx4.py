from urllib import request
import urllib
from bs4 import BeautifulSoup

# 날씨  xml 읽기
target = urllib.request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
# 페이지 파싱
soup = BeautifulSoup(target,'html.parser')
# print(soup)

# location 태그 찾기
for location in soup.select('location'):
    print("도시 : ",location.select_one('city').string)
    print("날씨 : ",location.select_one('wf').string)
    print("최저기온 : ",location.select_one('tmn').string)
    print("최고기온 : ",location.select_one('tmx').string)
    print("-------------------------------------")
