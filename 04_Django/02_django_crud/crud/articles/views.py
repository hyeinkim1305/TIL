from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
  	#  모든 게시글 조회
	# articles = Article.objects.all()[::-1]		# 순서가 뒤집어짐
	articles = Article.objects.order_by('-pk')		# pk의 역순으로 
	context = {
		'articles' : articles,
  	}
  # 이렇게 해야 templates/articles로 들어감. 그 setting에 등록된 앱 순서와 상관 없어짐 
	return render(request, 'articles/index.html', context)

def new(request):
	return render(request, 'articles/new.html')

def create(request):
    # 1. new.html 로 부터 전송된 데이터 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. 받은 데이터를 DB에 저장하기
    # 2-1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2-2
    article = Article(title=title, content=content)
    article.save()

    # 2-3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
