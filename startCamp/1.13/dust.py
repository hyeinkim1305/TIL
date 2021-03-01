import requests

key = 'mbsr22ZxsnSdYzgWL6ZEXF8zchZReHHj06FVrZEaYhzLx14roDMN0DLdr%2FCNzC4K5i1s3UmmeNZ3VEvoGtg0%2BQ%3D%3D'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=2&sidoName=서울&ver=1.0&returnType=json'
response = requests.get(url).json()
print(response)
item = response.get('response').get('body').get('items')[9]       ### 1.14에 배운거랑 다르게 get으로 가져왔네! 두 표현 다 알아두기!
time = item.get('dataTime')
station = item.get('stationName')
dust = int(item.get('pm10Value'))

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust}입니다.')

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if dust > 150:
    print('매우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust > 50:
    print('보통')
else:
    print('적음')
    