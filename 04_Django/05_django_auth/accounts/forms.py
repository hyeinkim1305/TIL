from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):     # UserChangeForm의 회원정보의 가짓수가 너무 많아서 줄인것 

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
