from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
	articles = Article.objects.all()
	context = {
		'articles' : articles,
	}

	return render(request, 'articles/index.html', context)

# def new(request):
# 	return render(request, 'articles/new.html')

# def new(request):		# 그럼 최종적으로는 이게 없어도 되는듯
# 	form = ArticleForm()
# 	context = {
# 		'form' : form,
# 	}
# 	return render(request, 'articles/new.html', context)

def create(request):
	if request.method == 'POST':		# POST로 요청 왔을 떄 실행하고
		form = ArticleForm(request.POST)		# titl, content 등 사용자가 입력한거 받아옴
		if form.is_valid():		# 값이 잘 넘어왔는지 확인
			article = form.save()		# form을 저장해서 article 변수에 담음 
			return redirect('articles:detail', article.pk) 
		return redirect('articles:index')
	else:
		form = ArticleForm()		# context 왜 빠져있는건지 생각해보기(그래야 유효하징 않은게 )
	context = {				
		'form' : form,
	}
	return render(request, 'articles/create.html', context)

	# article = Article()
	# article.title = request.POST.get('title')
	# article.content = request.POST.get('content')
	# article.save()

	# 다른 방법 
	# title = request.POST.get('title')
	# content = request.POST.get('content')
	# article = Article(title=title, content=content)
	# article.save()
	
	# 또 다른 방법
	# title = request.POST.get('title')
	# content = request.POST.get('content')
	# Article.objects.create(title=title, content=content)
	

def detail(request, pk):
	article = Article.objects.get(pk=pk)
	context = {
		'article' : article,
	}
	return render(request, 'articles/detail.html', context)

def delete(request, pk):
	article = Article.objects.get(pk=pk)
	if request.method == 'POST':
		article.delete()
	return redirect('articles:index')

# def edit(request, pk):
# 	article = Article.objects.get(pk=pk)
# 	context = {
# 		'article' : article,
# 	}
# 	return render(request, 'articles/edit.html', context)

# def update(request, pk):
# 	article = Article.objects.get(pk=pk)
# 	article.title = request.POST.get('title')
# 	article.content = request.POST.get('content')
# 	article.save()
# 	return redirect('articles:detail', article.pk)

def update(request, pk):
	article = Article.objects.get(pk=pk)		# new와의 차이는 이것 
	if request.method == 'POST':
		# 여기 pk정보가 instance로 안들어가면 새롭게 생성되는 과정으로 된다. 
		form = ArticleForm(request.POST, instance=article)		# Post요청으로 들어온 데이터를 넣는다
		if form.is_valid():
			article = form.save()
			return redirect('articles:detail', article.pk)
	else:
		form = ArticleForm(instance=article)		# form이 만들어지는것
	context = {
		'form' : form,
		'article' : article,
	}
	return render(request, 'articles/update.html', context)
