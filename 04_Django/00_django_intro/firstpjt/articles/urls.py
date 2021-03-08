from django.urls import path
# 명시적 상대 경로 표현 (.은 현재 경로를 의미)
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),    # end슬래시 / 를 꼭 입력
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name="hello"),
    path('introduce/<str:name>/<int:age>/', views.introduce, name="introduce"),
]
