from django.db import models

# Create your models here.

class Article(models.Model):
	# CharField는 길이에 제한이 있는 텍스트필드인것
	title = models.CharField(max_length=10)		# 컬럼 (PK는 제외하고 작성 / PK는 자동으로 만들어짐)
	content = models.TextField()		# 컬럼
	created_at = models.DateTimeField(auto_now_add=True)	# 작성일, auto_now_add인거 밑에꺼랑 헷갈리지 않게 주의
	updated_at = models.DateTimeField(auto_now=True)	# 수정일

	def __str__(self):
		return self.title
