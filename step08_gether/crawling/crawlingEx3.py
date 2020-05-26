# 1------------------------------
# source = '''<li>123</li>
# <li>가나다</li>
# <li>마바사</li>
# <li>abc</li>
# <li>kbs</li>
# <style>style</style>
# <!-- 주석 -->'''
#
# text=''
# # print(source[source.find("<"):])
# while True:
#     source = source[source.find("<"):]       # 태그 시작 찾기
#     if source.find('<--') == 0:
#         source=source[source.find('-->')+3]  # 찾는자리에서 3개를 지나가라 # 주석 내용 건너뛰기
#     elif source.find('<script>') == 0:
#         source = source[source.find('</script>') + 9]  # 스크립트 내용 건너뛰기
#     else:
#         source = source[source.find('>')+1:]  # 종료 찾기
#         for ch in source: # 태그 종료 이후 부터 한글자씩 가져오기
#             if ch=='<':
#                 break     # 다시 '<' 동작하면 종료
#             elif ch=='\t' or ch == '\n':
#                 continue  # 필요 없을 때 (text에 저장하지 않고 지나감)
#                 # text += ch
#             else:
#                 text += ch
#
#         if text.endswith(' ') == False:
#             text += ' '  # 구분자로 공백추가
#
#     if source.find('<') == -1 :
#         break
#
# # print(text) # 123 가나다 마바사 abc kbs style
# # lst = list(text.split())
# lst = text.split()  # 추출한 텍스트 문자열을 공백 단위로 분리
# print(lst)
# print(lst.__len__())
# print(type(lst))

# 2.--------------------------------------------------
import requests
text=''
req=requests.get('https://www.naver.com')
source = req.text
# print(source
# )
while True:
    source = source[source.find("<"):]       # 태그 시작 찾기
    if source.find('<--') == 0:
        source=source[source.find('-->')+3]  # 찾는자리에서 3개를 지나가라 # 주석 내용 건너뛰기
    elif source.find('<script>') == 0:
        source = source[source.find('</script>') + 9]  # 스크립트 내용 건너뛰기
    else:
        source = source[source.find('>')+1:]  # 종료 찾기
        for ch in source: # 태그 종료 이후 부터 한글자씩 가져오기
            if ch=='<':
                break     # 다시 '<' 동작하면 종료
            elif ch=='\t' or ch == '\n':
                continue  # 필요 없을 때 (text에 저장하지 않고 지나감)
                # text += ch
            else:
                text += ch

        if text.endswith(' ') == False:
            text += ' '  # 구분자로 공백추가

    if source.find('<') == -1 :
        break

# print(text) # 123 가나다 마바사 abc kbs style
# lst = list(text.split())
lst = text.split()  # 추출한 텍스트 문자열을 공백 단위로 분리
print(lst)
print(lst.__len__())
print(type(lst))
