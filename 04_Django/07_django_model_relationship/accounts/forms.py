from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

# 커스텀하고 migrtions파일들 지우고 다시 migration하고나서 usercreationform과 userchangeform은 다시 forms.py에서 재정의
# 해야한다. 
class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = get_user_model()            # 이게 원래 User인데 커스텀하면 get_user_model()로 바꿔준다!
        fields = UserCreationForm.Meta.fields