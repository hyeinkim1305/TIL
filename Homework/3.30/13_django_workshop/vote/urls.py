from django.urls import path
from . import views

app_name = 'vote'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comment_create/', views.comment_create, name='comment_create'),
    path('random_page/', views.random_page, name="random_page"),
]
