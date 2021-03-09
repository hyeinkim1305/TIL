from django.urls import path
# 명시적 상대 경로 표현 (.은 현재 경로를 의미)
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),    # end슬래시 / 를 꼭 입력
    path('greeting/', views.greeting, name='greeting'),     # 인사
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name="hello"),
    path('introduce/<str:name>/<int:age>/', views.introduce, name="introduce"),
    path('image/', views.image, name="image"),      # 이미지 랜덤으로 보여주는거
    path('fakegoogle/', views.fakegoogle, name="fakegoogle"),       # 페이크구글
    path('multiple/', views.multiple, name="multiple"),     # 숫자 두개 곱셈 입력받는거
    path('multiple_catch/', views.multiple_catch, name="multiple_catch"),    # 숫자 두개 곱셈해서 보여주는거 
    path('multiply/<int:num1>/<int:num2>', views.multiply, name="multiply"),    # 숫자 두개 받아서 곱하는거 교수님풀이
    path('dtl_practice/', views.dtl_practice, name="dtl_practice")      # dtl 예시
]
