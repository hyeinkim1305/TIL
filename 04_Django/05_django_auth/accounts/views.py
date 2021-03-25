from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login # 세션을 create해줌
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash        # 비번 변경시 바로 로그아웃되어버리는거 방지하려고 import
from .forms import CustomUserChangeForm     # UserchangeForm을 커스터마이징 한 것
from django.contrib.auth import get_user_model      # 유저 목록 보여주기 위함

# 유저 목록을 보여주는 함수
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

# 로그인 함수
def login(request):	
    # get 일때는 login 페이지를 주고,
	# post 일때는 login 을 하면 됨
    if request.user.is_authenticated:   	# T / F
        # 로그인된 사용자라면
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)	# request받은 다음에 데이터받음
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션 CREATE / save가 아니라 로그인 해주는 함수가있음 
            auth_login(request, form.get_user())        # request와 user객체를 받음
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm() # 인스턴스 생성
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃 함수
@require_POST       # url로 요청보내서 할 수 는 없다
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

# 회원가입 함수
def signup(request):
    if request.user.is_authenticated:
        # 로그인된 사용자라면
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Usercreationform이 성공적으로 끝나면 리턴은 user
            # 회원가입 후 바로 로그인 해주려고
            auth_login(request, user)       # UserCreatoinFrom의 save가 리턴하는게 user이기 때문에 user가 들어간 것 
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# 탈퇴 함수
@require_POST
def delete(request):
    if request.user.is_authenticated:
        # 만약 탈퇴하는 사용자의 세션 또한 삭제하고 싶다면 탈퇴 후 로그아웃 함수 호출
        # [주의] "탈퇴 후 로그아웃"의 순서가 바뀌면 안됨 
        # 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어짐
        request.user.delete()
        auth_logout(request)        # delete해도 session id가 남기 때문에 logout까지 시켜야함!
    return redirect('articles:index')

# 회원정보 수정 함수
@login_required     # 이거는 로그인 할 수 있는 곳으로 경로를 보내버림
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

# 비밀번호 변경 함수
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 비번 변경하고 로그아웃 되는거 방지하고자 넣음 
            user = form.save()
            update_session_auth_hash(request, user)     # Passwordchangeform의 부모클래스 Set어쩌구함수의 리턴은 Self.user
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)     # 기존 패스워드 정보가 있어야해서
    context = {
        'form' : form,
    }
    return render(request, 'accounts/password_change.html', context)

