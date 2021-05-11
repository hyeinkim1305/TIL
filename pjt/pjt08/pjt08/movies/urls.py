from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('<int:movie_pk>/review/', views.review_create),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('comments/', views.comment_list),
    path('<int:review_pk>/comment/', views.comment_create),
]
