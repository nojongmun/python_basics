# 선수과목
# html, css, javascript

from bs4 import BeautifulSoup
# html을 데려올때 파일을 읽어도 되고
# urllib 또는 request를 이용하여 웹에서 소스를 데려와도 됨

# 1. html  파일 읽기 처리 ------------------------
with open('sample.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, "html.parser")
# html 소스를 파이썬 내장 파서로 전달하여 html 코드를 해석
# print(soup)

# 2. html  파일 출력 처리 ------------------------
with open('sample.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    all_divs=soup.find_all('div')
# print(all_divs)
# print(type(all_divs))
# -------------------------------
#   find() : 해당 조건에 맞는 태그 하나를 데려오기, 중복이면 첫번째 태그 리턴
    first_div = soup.find('div')
print(first_div)

# ---------------------------------


