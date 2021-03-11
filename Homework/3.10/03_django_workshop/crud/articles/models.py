from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()

	def __Str__(self):		# 이 객체가 뭔지 알려줌 (레코드에 대한 정보를 사용자에게 바로 알려줌 )
		return self.title