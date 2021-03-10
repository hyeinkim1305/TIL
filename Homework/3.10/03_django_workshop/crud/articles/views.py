from django.shortcuts import render
from .models import Article   # 이거 새로 쓴거임

# Create your views here.

def index(request):
	articles = Article.objects.all()[::-1]
	context = {
		'articles' : articles,
	}
	
	return render(request, 'articles/index.html', context)

def new(request):
	return render(request, 'articles/new.html')
	
def create(request):
	title = request.GET.get('title')
	content = request.GET.get('content')

	article = Article(title=title, content=content)
	article.save()

	return render(request, 'articles/create.html')