from django import forms
from .models import Article, Comment        ### Comment 추가


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
        

### 추가
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)      # article은 빼고 form을 해줘야함 



