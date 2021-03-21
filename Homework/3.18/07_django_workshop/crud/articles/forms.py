from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	title = forms.CharField(
		label = '제목',
		widget = forms.TextInput(
			attrs={
				'class' : 'my-title form-control',
				'placeholder' : '제목을 입력하시오',
				'maxlength' : 10,
			}
		),
		error_messages={
			'required' : '제목 입력 필수',
		}
	)
	content = forms.CharField(
		label = '내용',
		widget = forms.Textarea(
			attrs = {
				'class' : 'my-content form-control',
				'placeholder' : '내용을 입력하시오',
				'rows' : 5,
				'cols' : 30,
			}
		),
		error_messages={
			'required' : '내용 입력 필수',
		}
	)

	class Meta:
		model = Article
		fields = '__all__'