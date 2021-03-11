from django.contrib import admin
# from . import models
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)	# list_display : 정해진 클래스 변수명



admin.site.register(Article, ArticleAdmin)

# admin site에 Article클래스를 register하겠다.
