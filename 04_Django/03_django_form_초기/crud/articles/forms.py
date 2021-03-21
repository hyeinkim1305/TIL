from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	title = forms.CharField(
		label = '제목',
		widget = forms.TextInput(
			attrs={
				'class' : 'title',
				'palceholder' : 'Enter the titile',
				'max_length' : 10,
			}
		)
	)
	content = forms.CharField(
		label = '내용',
		widget = forms.Textarea(
			attrs={
				'class' : 'content',
				'palceholder' : 'Enter the content',
			}
		)
	)

	class Meta:
		model = Article
		fields = '__all__'
		# exclude = ('title', )



# class ArticleForm(forms.Form):
# 	REGIONS = [
# 		('sl', '서울'),
# 		('dj', '대전'),
# 		('gj','광주'),
# 		('gm', '구미'),
# 	]
# 	title = forms.CharField(max_length=10)
# 	content = forms.CharField(widget=forms.Textarea)	# 여러줄들어가는거
# 	region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect())
	
