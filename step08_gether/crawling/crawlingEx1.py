# requests 와 BeautifulSoup4 사용 : setting - project-interperint에서 추가
# 1. 원하는 웹 페이지에 request 를 보낸다.
# 2. 받은 html 을 파싱한다.
# 3. 필요한 정보를 추출한다.

import requests as req

def get_html(url):
    html = ""
    res = req.get(url)
    if res.status_code == 200 : # 정상수신
        html = res.text
    return html


from bs4 import BeautifulSoup
url="https://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=1"
html = get_html(url)
# print(html)
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# BeautifulSoup : 파이썬용 html, xml 파서 (구분분석)
# html 데이터를 추출하는 용도로 사용



