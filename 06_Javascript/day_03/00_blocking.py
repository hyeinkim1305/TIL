from time import sleep
import requests

# 1. sleep
# 3초간 슬립
def sleep_3_seconds():
    sleep(3)
    print('잘잤다')

print('이제 자야지')
sleep_3_seconds()
print('학교가자')


# 2. requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1/')
# 파싱
todo = response.json()

print(todo)
