from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 커스텀 모델 대체
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')          # 대칭을 비활성화해버린다. 

