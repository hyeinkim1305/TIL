from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Vote, Comment
from .forms import VoteForm, CommentForm
import random

# Create your views here.

def index(request):
    votes = Vote.objects.order_by('-pk')
    context = {
        'votes' : votes,
    }
    return render(request, 'vote/index.html', context)

def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        vote = form.save()
        return redirect('vote:detail', vote.pk)
    else:
        form = VoteForm()
    context = {
        'form' : form,
    }
    return render(request, 'vote/create.html', context)

def detail(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    comment_form = CommentForm()                # 댓글 작성 form
    comments = vote.comment_set.all()           # 모든 댓글 불러오기
    comments_count = vote.comment_set.all().count()
    comments_blue = vote.comment_set.all().filter(pick=0).count()
    comments_red = vote.comment_set.all().filter(pick=1).count()
    if comments_blue != 0 and comments_blue != 100:
        comments_ratio_b = comments_blue / comments_count * 100
        comments_ratio_r = 100 - comments_ratio_b
    else:
        comments_ratio_b = comments_blue
        comments_ratio_r = comments_red
    context = {
        'vote' : vote,
        'comment_form' : comment_form,
        'comments' : comments,
        'comments_ratio_b' : comments_ratio_b,
        'comments_ratio_r' : comments_ratio_r,
        
    }
    return render(request, 'vote/detail.html', context)

@require_POST
def comment_create(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.vote = vote
        comment.save()
        return redirect('vote:detail', vote.pk)
    context = {
        'comment_form' : comment_form,
        'vote' : vote,
    }
    return render(request, 'vote/detail.html', context)


def random_page(request):
    num = Vote.objects.values('id')
    number = random.choice(num)['id']
    return redirect('vote:detail', number)