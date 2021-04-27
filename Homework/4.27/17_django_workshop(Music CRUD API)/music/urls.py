from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artists_show),
    path('artists/<int:artist_pk>/', views.artists_detail),
    path('artists/<int:artist_pk>/music/', views.artists_music),
    path('music/', views.music_show),
    path('music/<int:music_pk>', views.music_detail),

]
