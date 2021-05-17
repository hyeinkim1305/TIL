from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path
from . import views

# token 위에 import 한거 설치해야함
urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
]
