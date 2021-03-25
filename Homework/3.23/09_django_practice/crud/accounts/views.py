from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm		# form
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm		# update의 Form
# 다른 접근일 떄 제한 
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# 패스워드 변경시 로그아웃 되는거 방지
from django.contrib.auth import update_session_auth_hash


def index(request):
	return render(request, 'accounts/index.html')

def signup(request):
	if request.user.is_authenticated:		# 이미 로그인 되어있으면 회원가입안됨
		return redirect('accounts:index')

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('accounts:index')
	else:
		form = UserCreationForm()
	context = {
		'form' : form,
	}
	return render(request, 'accounts/signup.html', context)


def login(request):
	if request.user.is_authenticated:		# 이미 로그인 되어있으면 다른 곳으로
		return redirect('accounts:index')

	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			auth_login(request, form.get_user())		# request와 user객체를 받는 로그인 함수
			return redirect(request.GET.get('next') or 'accounts:index')
	else:
		form = AuthenticationForm()
	context = {
		'form' : form,
	}
	return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
	auth_logout(request)
	return redirect('accounts:index')


@require_POST
def delete(request):
	if request.user.is_authenticated:
		request.user.delete()
		auth_logout(request)
	return redirect('accounts:index')

@login_required
def update(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('accounts:index')
	else:
		form = CustomUserChangeForm()
	context = {
		'form' : form,
	}
	return render(request, 'accounts/update.html', context)

def password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)		# 비번 변경시 로그아웃 되는거 방지
			return redirect('accounts:index')

	else:
		form = PasswordChangeForm(request.user)
	context = {
		'form' : form,
	}
	return render(request, 'accounts/password.html', context)
