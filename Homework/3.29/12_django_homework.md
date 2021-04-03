# 12_django_homework



### 1. 1:N True or False

```
1. T
2. F 역참조
3. T
4. F 반드시 일 필요는 없다
```



### 2. ForeignKey column name

```
컬럼의 이름 : answer_id
테이블의 이름 : articles_comment
```



### 3. 1:N model manager

```
question.comment_set.all
```



### 4. next parameter

HTTP ERROR 405가 발생한다.

```python
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if request.user == article.user:
            article.delete()
        else:
            return redirect('articles:detail', article.pk)
    return redirect('articles:index')
```

login required 대신 if request.user.is_authenticated를 추가한다.  