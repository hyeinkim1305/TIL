from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article, Comment    ###
from .forms import ArticleForm, CommentForm     ###


@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


### detail에서는 (세부 article, 댓글입력form, 지금까지 작성된 댓글) 불러와야함
@require_safe       
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()        ### 추가
    comments = article.comment_set.all()        ### 
    context = {
        'article': article,
        'comment_form' : comment_form,      ### 
        'comments' : comments,      ###
    }
    return render(request, 'articles/detail.html', context)



@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
        

### 추가 # 여기부분 강의 다시 들어보기
@require_POST
def comment_create(request, article_pk):
    if request.user.is_authenticated:
        # 이미 get요청은 detail에서 걸러졌으니까 POST일때만 신경쓰면 되는듯
        article = get_object_or_404(Article, pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article       # 이거 약간 이해 안됨
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {     # 여기 왜 해준다고/??
            'comment_form' : comment_form,
            'article' : article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')

### 추가
@require_POST
def comment_delete(request, article_pk, comment_pk):
    # 이 함수를 실행할 때는 article과 comment가 이미 html에서 있음 
    # 지울 댓글만 찾아오기
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)