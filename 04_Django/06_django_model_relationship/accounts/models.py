from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 대체해준것!!
# 중간에 시작했으면 DB 다 삭제하고 새로 마이그레이션 해야함
# 1. 모든 설계도 재우기 (migrations)
# 2. DB.sqlite 지우기
class User(AbstractUser):     # user 를 customizing 해준 것이다. 
  pass