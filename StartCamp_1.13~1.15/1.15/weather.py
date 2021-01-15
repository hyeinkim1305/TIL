import requests
from pprint import pprint

url = 'https://www.metaweather.com/api/location/1132599/'
response = requests.get(url).json()
# pprint(response)

location = response['title']
date = response['consolidated_weather'][0]['applicable_date']
weather = response['consolidated_weather'][0]['weather_state_name']
min_temp = response['consolidated_weather'][0]['min_temp']
max_temp = response['consolidated_weather'][0]['max_temp']
# 오늘 기상 정보
print(f'{date}, {location}의 기상정보는 {weather}이며 최고온도는 {max_temp}이고 최저온도는 {min_temp}입니다.')

# 6일간 기상 정보
# 내풀이
for i in range(6):
    date = response['consolidated_weather'][i]['applicable_date']
    weather = response['consolidated_weather'][i]['weather_state_name']
    min_temp = response['consolidated_weather'][i]['min_temp']
    max_temp = response['consolidated_weather'][i]['max_temp']
    print(f'{date}, {location}의 기상정보는 {weather}이며 최고온도는 {max_temp}이고 최저온도는 {min_temp}입니다.')

# 교수님 풀이
weathers = response['consolidated_weather']
for i in weathers:
    date = i['applicable_date']
    weather = i['weather_state_name']     ### round 하고 (~,1)은 소수점 첫째 자리까지 나타냄
    max_temp = round(i['max_temp'],1)
    print(f'{date}, {location}의 기상정보는 {weather}이며 최고온도는 {max_temp}이고 최저온도는 {min_temp}입니다.')