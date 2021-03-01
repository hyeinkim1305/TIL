# import requests

# url = 'https://api.agify.io?name=michael'
# response = requests.get(url).json()
# name = response['name']
# age = response['age']
# print(type(response))
# print(response)
# print(f'저는 {name}이고, 나이는{age}입니다.')

import requests

url = 'https://api.nationalize.io?name=michael'
response = requests.get(url).json()
name = response['name']
print(response)
country_id = response['country'][0]['country_id']
country_probability = response['country'][0]['probability'] * 100

print(f'{name}의 국적은 {country_id}일 가능성이 {country_probability}% 입니다.')