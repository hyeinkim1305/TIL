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

