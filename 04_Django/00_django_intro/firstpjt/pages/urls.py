from django.urls import path
from . import views

app_name = 'pages'  # 해준 이유: 
urlpatterns = [
    path('index/', views.index, name="index")
]
