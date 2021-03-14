from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'overview', 'poster_path',)      
admin.site.register(Movie, MovieAdmin)      # 여기 꼭 등록해야함