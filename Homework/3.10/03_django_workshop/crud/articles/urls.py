from django.urls import path    # 새로 쓴 거임
from . import views   # 이것도

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
