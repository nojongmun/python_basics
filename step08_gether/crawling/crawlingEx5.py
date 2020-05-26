# https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20191101
# find('a').text  제목 추출
# crawlingEx2.py 참고
from bs4 import BeautifulSoup
from urllib import request
import urllib

soup=BeautifulSoup(urllib.request.urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20191101").read(), 'html.parser')

# 내가 푼 것
# print(soup)
# print(soup.find('tbody').find_all('a'))

# for i in soup.find('tbody').find_all('a'):
#     if i.get('title') is None: # 널 값 처리
#         continue
#     else:
#        print(i.get('title'))

# 강사님 해설
# print(soup.find('div',{'class':'tit5'}))
# print(soup.find('div',{'class':'tit5'}).find('a').text)

# print(soup.find_all('div',{'class':'tit5'}))
# print(soup.find_all('div','tit5'))

for i in soup.find_all('div','tit5'):
   print(i.find('a').text)



