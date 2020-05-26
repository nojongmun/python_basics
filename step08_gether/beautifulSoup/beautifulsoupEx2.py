from bs4 import BeautifulSoup
print('-----------  태그와 속성을 이용하여 데리고 오기 ------------')
# find_all('태그명',{'속성명':'값',...})
# find('태그명',{'속성명':'값',...})

# <div> 에서 id 속성의 값이 sample_id 인 것 데려오기
with open('sample.html', encoding='utf-8') as fp:   # 한글이 있는 경우 encoding='utf-8' 넣기
    soup = BeautifulSoup(fp, 'html.parser')
    sample_id_div = soup.find('div', {'id':'sample_id'})
    print(sample_id_div)

print('-----------  html 구조을 이용하여 데리고 오기 ------------')
with open('sample.html', encoding='utf-8') as fp:   # 한글이 있는 경우 encoding='utf-8' 넣기
    soup = BeautifulSoup(fp, 'html.parser')
#   id = 'sample_id인 div 태그 가져오기
    sample_id_divs = soup.find('div', {'id':'sample_id'})
#   그 태그 안에서 p 태그 가져오기
    all_ps_sample_p_sample_id_divs = sample_id_divs.find_all('p')
    print(all_ps_sample_p_sample_id_divs)

    print('-'*50)
    temp = soup.find_all('p')
    print(temp)  # p 태그 전체 추출

