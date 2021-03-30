from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)        # 1:N에서 N 쪽에 foreignkey 생긴다. 
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 댓글은 articles의 model에 구조 만듬
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)          # 참조하는 모델의 소문자 넣어준다
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):      # shell_plus에서 댓글이 보이게 하기 위함
        return self.content

