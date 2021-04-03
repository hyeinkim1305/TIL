from django import forms
from .models import Vote, Comment

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'


class CommentForm(forms.ModelForm):
    PICKS = [
        (False, 'BLUE'),
        (True, 'RED'),
    ]
    pick = forms.ChoiceField(choices=PICKS)
    class Meta:
        model = Comment
        fields = ('pick', 'content',)
