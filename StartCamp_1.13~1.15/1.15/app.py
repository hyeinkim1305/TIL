from flask import Flask
import random
from datetime import datetime
app = Flask(__name__)

@app.route('/') 
def hello_world():
    return 'Hello, World!'

@app.route('/ssafy')   
def ssafy():
    return 'This is SSAFY!??????'

@app.route('/lotto')
def lotto():
    numbers = range(1,46)
    lucky = random.sample(numbers,6)
    return f'{lucky}'

@app.route('/today')
def today():
    today = datetime.now()
    return f'오늘은 {today}!'

@app.route('/dday')
def dday():
    today = datetime.now()
    endgame = datetime(2021,5,28)    ### 미래
    td = endgame - today
    return f'싸피 1학기 종료까지 {td.days}일 남았습니다.'

@app.route('/isitbirth')
def birth():
    today = datetime.now()
    birthday = datetime(2021, 5, 13)
    if (today.month == birthday.month) and (today.day == birthday.day):
        return f'오늘은 {birthday.month}월 {birthday.day}일 생일입니다.'
    else:
        return f'오늘은 생일이 아닙니다.'

@app.route('/greeting/<name>')   ### <>는 가변변수
def greeting(name):
    return f'반갑습니다,{name}입니다.'

@app.route('/posts/<int:number>')
def post(number):
    return f'{number}번 글입니다.'

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다.'

@app.route('/even/<int:number>')
def even(number):
    if number % 2 ==1:
        msg = '홀수'
    else:
        msg = '짝수'
    return msg

if __name__ == '__main__':
    app.run(debug=True)