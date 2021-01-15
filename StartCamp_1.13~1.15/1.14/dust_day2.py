import requests
from pprint import pprint

API_KEY = 'private'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={API_KEY}&returnType=json&numOfRows=10&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
response = requests.get(url).json()

pprint(response)          # pprint하면 깔끔하게 정리돼서 나옴 (이 점이 1.13 dust랑 다르네)
print(type(response))

# 강남대로 데이터 보기
time = response['response']['body']['items'][9]['dataTime']
stationName = response['response']['body']['items'][9]['stationName']
dust = int(response['response']['body']['items'][9]['pm10Value'])

print(time)
print(stationName)
print(dust)

print(f'{time}시 기준 {stationName}의 미세먼지 농도는 {dust}입니다.')

if dust > 150:
    grade = '매우나쁨'
elif dust > 80:
    grade = '나쁨'
elif dust > 30:
    grade = '보통'
else:
    grade = '좋음'

print(f'{time}시 기준 {stationName}의 미세먼지 농도는 {dust}이며 {grade} 수준입니다.')

