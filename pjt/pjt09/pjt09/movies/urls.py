from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended', views.recommended, name='recommended'),
    path('recommended/<int:genre_pk>/', views.genre_recommended, name='genre_recommended'),
]
