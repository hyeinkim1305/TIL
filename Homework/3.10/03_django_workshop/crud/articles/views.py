from django.shortcuts import render, redirect
from .models import Article   # 이거 새로 쓴거임

# Create your views here.

def index(request):
	articles = Article.objects.all()[::-1]
	context = {
		'articles' : articles,
	}
	
	return render(request, 'articles/index.html', context)	# 이렇게 하면 installed_apps에 추가한 순서와 상관없음 

def new(request):
	return render(request, 'articles/new.html')
	
def create(request):		# DB저장이 주 목적
	title = request.POST.get('title')
	content = request.POST.get('content')

	article = Article(title=title, content=content)
	article.save()

	# return render(request, 'articles/create.html')
	return redirect('articles:detail', article.pk)		# 이렇게 하면 저장되고 index로 돌아와 

	# create 하고 만약 index.html로 보내면 index함수가 실행이 안됨. 따라서 index url로 다시 
	# 신호를 보내줘야함 

def detail(request, pk):
	article = Article.objects.get(pk=pk)		# 뒤에 pk가 url에서 넘어온것 / 작성한 글꺼 pk 넘어와
	context = {
		'article' : article,
	}
	return render(request, 'articles/detail.html', context)


def delete(request, pk):
	article = Article.objects.get(pk=pk)
	if request.method == 'POST':
		article.delete()
		return redirect('articles:index')
	else:
		return redirect('articles:detail', article.pk)

def edit(request, pk):
	article = Article.objects.get(pk=pk)
	context = {
		'article' : article,
	}
	return render(request, 'articles/edit.html', context)

def update(request, pk):
	article = Article.objects.get(pk=pk)	# 기존꺼 보여줘야함
	article.title = request.POST.get('title')
	article.content = request.POST.get('content')
	article.save()		# 덮어씌어짐 

	return redirect('articles:detail', article.pk)
