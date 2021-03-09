from django.urls import path
from . import views

app_name = 'pages'  # 해준 이유: 아마 articles꺼와 index 별개로 하려고 
urlpatterns = [
    path('index/', views.index, name="index")
]
