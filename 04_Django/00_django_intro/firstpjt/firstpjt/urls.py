"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include       # include를 가져온 다음 
# from articles import views as article_views     # artlcles패키지의 views모듈의 index함수, greeting함수 호출하기
# from pages import views as pages_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index),    # end슬래시 / 를 꼭 입력
    # path('greeting/', views.greeting),
    # path('dinner/', views.dinner),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    path('articles/', include('articles.urls')),        # articles로 들어오는 경로는 articles.urls로 가
    path('pages/', include('pages.urls')),
]       # path함수 2번째 인자는 어떤 view를 보여줄지 생각
