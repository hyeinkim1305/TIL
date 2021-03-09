import random
from django.shortcuts import render

# Create your views here.
# 메인페이지를 보여주는 역할
def index(request):   # view함수에 첫번째 인자는 반드시 request이어야함
    return render(request, 'articles/index.html')    # render의 첫 인자도 반드시 request

def greeting(request):
    foods = ['apple','banana','coconut',]
    info = {
        'name' : 'Harry'
    }
    context = {
        'name' : info,
        'foods' : foods,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['족발', '피자', '햄버거', '초밥']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # thorw에서 보낸 request 중 message이름의 것이 있다면 가져와서 message변수에 넣어줘
    message = request.GET.get('message')  # Get메서드 안에 get이 있는것 /
    # print(message)
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)

def introduce(request, name, age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'articles/introduce.html', context)

# 이미지 랜덤으로 보여주는 페이지
def image(request):
    return render(request, 'articles/image.html')

# 페이크구글
def fakegoogle(request):
    return render(request, 'articles/fakegoogle.html')

# 숫자 두개 곱할거 받는 함수
def multiple(request):
    return render(request, 'articles/multiple.html')
# 숫자 두개 곱하고 보여주는거
def multiple_catch(request):
    multiple1 = request.GET.get('multiple1')        # request중에 multiple1이라고 온거 받아
    multiple2 = request.GET.get('multiple2')
    ans = int(multiple1) * int(multiple2)
    context = {
        'answer' : ans
    }
    return render(request, 'articles/multiple_catch.html', context)
# 숫자 두개 받아서 곱하는거 교수님풀이
def multiply(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result,
    }
    return render(request, 'articles/multiply.html', context)


def dtl_practice(request):
    foods = ['감자탕', '초밥', '치킨', '갈비탕', '파스타']
    fruits = ['키위', '망고', '파인애플', '귤']
    user_list = []
    context = {
        'foods' : foods,
        'user_list' : user_list,
        'fruits' : fruits,
    }
    return render(request, 'articles/dtl_practice.html', context)