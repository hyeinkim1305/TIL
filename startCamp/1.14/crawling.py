import requests
import bs4
url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser') # html.parser 넣어야 경고문 안뜸
exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(f'환율은 {exchange_rate.text} 입니다.')   ### exchange_rate.text  text 붙는거 기억하기!