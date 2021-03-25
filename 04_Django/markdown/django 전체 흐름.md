## 전체적인 순서

[TOC]

#### project

1. project 생성 > 서버 확인 > 앱 생성 > settings에 앱 등록

2. urls.py 생성 (앱 별로 다르게 하려면 )

3. 필요하다면, templates / base.html

#### app

1. models.py (저장할 DB 구조 만듬) 
2. forms.py 생성 ( 모델꺼 상속 or 상속 no)
3. urls.py (경로 나눠줌)
4. views.py (함수 혹은 그 보여줄거 생성) + decorator+get_object_or_404
5. templates / app / html
6. models.py작성 +  migrations 하자 (makemigrations > migrate > shell 해서 데이터 입력 )
7. admin 작성 (클래스 등록)  > createsuperuser 

** sqlite explorer는 마우스 오른쪽 눌러서 하는거

python -m venv venv   깃배쉬

vscode 켜고 shift ctrl P 눌러서 interpreter venv 로 설정

pip list 해보고 pip install -r requirements.txt 하기



## 세부 사항

#### Project

- **settings.py**

  > '앱이름', 'django_extensions' 등록 (extensions는 shell_plus하려고 쓰는것)
  >
  > ```
  > INSTALLED_APPS = [
  >     'articles',
  >     'django_extensions',
  >     ]
  > ```
  >
  > ko-kr
  >
  >  ```LANGUAGE_CODE = 'ko-kr'```

  > (상속시)  DIRS 수정
  >
  > ```'DIRS': [BASE_DIR/'crud'/'templates'],```

- **Urls.py** : 앱별로 경로 나눠주는 것

  > include 추가
  >
  > ```
  > from django.contrib import admin
  > from django.urls import path, include		# 이 부분
  > 
  > urlpatterns = [
  >     path('admin/', admin.site.urls),
  >     path('articles/', include('articles.urls')),	# 이 부분
  > ]
  > ```

- **templates > base.html**

  > (상속시) 
  >
  > CDN  /  block  /  ! tap / 추가로, div class='container'

#### App

- **models.py**

  > 클래스 지정 (데이터 구조 만듦)
  >
  > ```
  > from django.db import models
  > 
  > class Article(models.Model):		# 이 부분
  > 	title = models.CharField(max_length=10)
  > 	content = models.TextField()
  > 	created_at = models.DateTimeField(auto_now_add=True)
  > 	updated_at = models.DateTimeField(auto_now=True)
  > ```
  >
  > 이 객체가 뭔지 사용자에게 바로바로 알려줌 
  >
  > ```
  > def __str__(self):
  > 		return self.title
  > ```

- **urls.py**

  > 상세경로 + 만약 앱이 여러개면 앱이름 지정할 수 있음 
  >
  > ```
  > from django.urls import path
  > from . import views		# 이 부분 (상대경로)
  > 
  > app_name = 'articles'
  > urlpatterns = [
  >  path('index/', views.index, name='index'),
  >  path('new/', views.new, name='new'),
  >  path('create/', views.create, name='create'), # 내용입력시 넘어갈 url
  > ]
  > ```
  >
  > 여기서 ```path('', views.index, name='index')```하면 그냥 articles/로 해당 url 페이지 나옴  + urls.py에서 name을 붙였기때문에 다른 html에서 a태그로 경로 설정시 articles:index 이렇게 하면 됨!

- **views.py**

  > 함수생성 등 각종 처리
  >
  > 만약 앱 경로 안에 html 넣어줄거면 templates에 앱 이름 폴더하나 더 만들고 views 함수 return에서는 '앱이름/경로.html' 이런식으로 함
  >
  > ```python
  > from django.shortcuts import render
  > from .models import Article		# models에 있는거 가져와야함
  > 
  > def index(request):
  >   	#  모든 게시글 조회
  > 	# articles = Article.objects.all()[::-1]		# 순서가 뒤집어짐
  > 	articles = Article.objects.order_by('-pk')		# pk의 역순으로 
  > 	context = {
  > 		'articles' : articles,
  >   	}
  >   	# 이렇게 해야 templates/articles로 들어감. 그 setting에 등록된 앱 순서와 상관 없어짐 
  > 	return render(request, 'articles/index.html', context)
  > 
  > def new(request):
  > 	return render(request, 'articles/new.html')
  > 
  > def create(request):	# DB저장이 목적!!
  >     # 1. new.html 로 부터 전송된 데이터 받기
  >     title = request.GET.get('title')
  >     content = request.GET.get('content')
  > 
  >     # 2. 받은 데이터를 DB에 저장하기 (3가지 방법)
  >     # 2-1
  >     # article = Article()
  >     # article.title = title
  >     # article.content = content
  >     # article.save()
  > 
  >     # 2-2
  >     article = Article(title=title, content=content)
  >     article.save()
  > 
  >     # 2-3
  >     # Article.objects.create(title=title, content=content)
  > 
  >     return render(request, 'articles/create.html')
  > ```

- **templates > (앱 폴더이름) > html**

  > extends
  >
  > block
  >
  > form -> action에 url경로 'articles:create' 이런 식으로 
  >
  > ```
  > {% extends 'base.html' %}
  > {% block content %}
  > <h1>Articles</h1>
  > <a href="{% url 'articles:new' %}">글작성</a>  
  > <hr>
  > {% for article in articles  %}
  >  <h2>글 번호 : {{ article.pk }}</h2>
  >  <h2>글 제목 : {{ article.title }}</h2> 
  >  <h2>글 내용 : {{ article.content }}</h2>
  >  <hr>
  > {% endfor %}
  > {% endblock content %}
  > ```
  >
  > ```
  > {% extends 'base.html' %}
  > {% block content %}
  > 
  > <h1 class="text-center">New Article</h1>
  > <hr>
  > <form action="{% url 'articles:create' %}" method="GET">
  >  <label for="title">Title: </label>
  >  <input type="text" name="title" id="title"><br>
  >  <label for="content">Content: </label>
  >  <textarea name="content" id="content" cols="30" rows="10"></textarea> 
  >  <input type="submit" value="글작성">  
  > </form>
  > <hr>
  > <a href="{% url 'articles:index' %}">뒤로가기</a>
  > 
  > {% endblock content %}
  > ```
  >
  > 여기서 a태그는 form 태그 밖에 넣어줘야한다!
  
- **migrations**

  > 1. models.py
  >
  >    model 변경사항 발생
  >
  > 2. python manage.py makemigrations
  >
  >    migrations 파일 생성
  >
  > 3. python manage.py migrate
  >
  >    DB 적용

- **admin.py**

  >```
  >from django.contrib import admin
  >from .models import Article
  >
  >admin.site.register(Article)
  >```
  >
  >새로운 클래스 정의도 가능한듯
  >
  >```
  >from django.contrib import admin
  >from .models import Article
  >
  >class ArticleAdmin(admin.ModelAdmin):
  >	list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)	# list_display : 정해진 클래스 변수명
  >
  >admin.site.register(Article, ArticleAdmin)   # admin site에 Article, ArticleAdmin클래스를 register하겠다.
  >```
  >
  >admin계정 입력해야함
  >
  >```
  >$ python manage.py createsuperuser
  >Username (leave blank to use 'user'): admin
  >Email address:
  >Password:
  >Password (again):
  >Superuser created successfully.
  >```



## 추가 설정

-- 03_django_workshop 코드 참고 

- **form입력 내용 url에 노출 피하기**

  > 1. html파일
  >
  >    form에서 method='POST'로 바꾸고, {% csrf_token %} 추가
  >
  >    ```
  >    <form action="{% url 'articles:create' %}" method="POST">
  >        {% csrf_token %}
  >    ```
  >
  > 2. views.py
  >
  >    request.POST로 바꾸기
  >
  >    ```
  >    def create(request):
  >    	title = request.POST.get('title')
  >    	content = request.POST.get('content')
  >    ```
  >
  > ** 참고 : url상으로  ```http://127.0.0.1:8000/articles/create/?title=hehe``` 이런식으로 하는거는 url상으로 정보를 보내는 GET방식이다 **

- **함수실행 후 html이 아닌 다른 url경로로 리턴하기**

  > 원래는 url > view함수 > html 순서 인데, view함수에서 다른 url경로로 보내려면, 
  >
  > 1. views.py
  >
  >    ```
  >    from django.shortcuts import render, redirect
  >    
  >    return redirect('articles:index')
  >    ```
  >
  >    import에 redirect 추가,  return에 redirect하고 원하는 경로 적기
  >
  > 예를 들어 이렇게 하면 
  >
  > articles(html)페이지 > new (url) 경로로 이동 {articles:new} > new(views.py) 실행 > new (html) 에서 form태그에 입력하고  action 경로가 {articles:create} >  create(url) 이동 > create(views.py) 함수 실행 + DB 저장 + {articles:index}로 redirect > index(url) 경로로 이동 > index(views.py) 실행 + DB저장된거 부름 > index(html) 에서 보여줌 

- **글 작성시 바로 detail 페이지로 넘어가기**

  > 작성과 동시에 DB에 저장이 되니까 해당 작성 글 pk로 url에 접근한다.
  >
  > 1. 앱 / urls.py
  >
  >    ```
  >    path('<int:pk>/', views.detail, name='detail'),
  >    ```
  >
  >    path경로에 다음과 같이 추가
  >
  > 2. 앱 / views.py
  >
  >    ```
  >    def detail(request, pk):
  >    	article = Article.objects.get(pk=pk)		# 뒤에 pk가 url에서 넘어온것 / 작성한 글꺼 pk 넘어와
  >    	context = {
  >    		'article' : article,
  >    	}
  >    	return render(request, 'articles/detail.html', context)
  >    ```
  >
  >    detail 함수 생성 (url에서 받은 pk를 추가로 받아옴 )
  >
  >    ```
  >    # return 부분 변경해줘
  >    def create(request):		# DB저장이 주 목적
  >    	title = request.POST.get('title')
  >    	content = request.POST.get('content')
  >    
  >    	article = Article(title=title, content=content)
  >    	article.save()
  >    
  >    	# return render(request, 'articles/create.html')
  >    	return redirect('articles:detail', article.pk)	# 저장하고, detail url로 넘겨줘
  >    ```
  >
  >    글 작성 함수를 DB저장 후 return 할 떄 render가 아니라 redirect로 해서 detail url로 pk와 함께 보내줌
  >
  >    ⭐ return해서 detail로 보낼 때 article.pk랑 같이 넘겨주는거 중요 ⭐
  >
  > 3. 앱 / templates / detail.html
  >
  >    ```
  >    {% extends 'base.html' %}
  >    {% block content %}
  >    
  >      <h1 class="text-center">DETAIL</h1>
  >      <hr>
  >      <p>글 번호 : {{ article.pk }}</p>
  >      <p>글 제목 : {{ article.title }}</p>
  >      <p>글 내용 : {{ article.content }}</p>
  >      <hr>
  >      <a href="{% url 'articles:index' %}">[back]</a>
  >    
  >    {% endblock content %}
  >    ```
  >
  > => 글 작성한거를 new(html)에서 create로 보내주고 (views.py)에서 DB저장후 detail url로 보내줘서 함수로 해당 pk 글 가져와서 html에서 보여줌 

- **index에서 각 글마다 detail버튼이 있고 넘어가게 하려면**

  > 1. index.html 수정
  >
  >    ```
  >    {% extends 'base.html' %}
  >    {% block content %}
  >      <h1>INDEX</h1>
  >      <a href="{% url 'articles:new' %}">NEW</a>
  >      <hr>
  >      {% for article in articles  %}
  >        <h2>번호 : {{ article.pk }}</h2>
  >        <h2>제목 : {{ article.title }}</h2>
  >        <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
  >        <hr>
  >      {% endfor %}
  >    {% endblock content %}
  >    ```
  >
  >    articles:detail 로 article.pk와 함께 넘겨준다 + 여기는 comma가 없다 (html은 comma없고 함수는있음)
  >
  >    ⭐ return해서 detail로 보낼 때 article.pk랑 같이 넘겨주는거 중요 ⭐

- **내가 작성한 특정 게시글 삭제 후 인덱스로 돌아가기**

  > 1. 앱 / urls.py
  >
  >    ```
  >    path('<int:pk>/delete/', views.delete, name='delete'),
  >    ```
  >
  > 2. 앱 / views/py
  >
  >    ```
  >    def delete(request, pk):
  >    	article = Article.objects.get(pk=pk)
  >    	if request.method == 'POST':
  >    		article.delete()
  >    		return redirect('articles:index')
  >    	else:
  >    		return redirect('articles:detail', article.pk)
  >    ```
  >
  >    request.method가 POST일때만 삭제되도록 해야 아무나 지우는 것이 불가능하다
  >
  > 3. 앱 / templates / detail.html
  >
  >    ```
  >    	<form action="{% url 'articles:delete' article.pk %}" method="POST">
  >        {% csrf_token %}
  >        <button class="btn btn-danger">DEL</button>
  >        {% comment %} <input type="submit" value="DELL"> {% endcomment %}
  >      </form>
  >    ```
  >
  >    action에 저렇게 추가하고 POST로 요청방식 변경하면 아무나 접근해서 지우는 것이 불가능 
  >
  > ** 참고 : a 태그는 get방식만 가능하다

- **게시글 수정**

  > detail에서 수정버튼 누르고 수정할때는 기존 내용이 있는 상태이어야한다.
  >
  > 1. 앱 / urls.py
  >
  >    ```
  >    path('<int:pk>/edit/', views.edit, name='edit'),
  >    ```
  >
  > 2. 앱 / views.py
  >
  >    ```
  >    def edit(request, pk):
  >    	article = Article.objects.get(pk=pk)
  >    	context = {
  >    		'article' : article,
  >    	}
  >    	return render(request, 'articles/edit.html', context)
  >    ```
  >
  >    함수로 해당 pk 의 article 불러옴
  >
  > 3. 앱 / templates / edit.html
  >
  >    ```
  >    {% extends 'base.html' %}
  >    {% block content %}
  >    
  >      <h1 class="text-center">EDIT</h1>
  >      <hr>
  >      <form action="{% url 'articles:update' article.pk %}" method="POST">
  >        {% csrf_token %}
  >        <label for="title">TITLE : </label>
  >        <input type="text", name="title", id="title" value="{{ article.title }}"><br>
  >        <label for="content">CONTENT : </label>
  >        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea> <!--내용은 큰 인풋-->
  >        <input type="submit" value="글 수정">  
  >      </form>
  >      <hr>
  >      <a href="{% url 'articles:index' %}">BACK</a>     <!--index라는 이름 설정해놔서 가능 !!-->
  >    
  >    {% endblock content %}
  >    ```
  >
  >    new 와 edit의 차이는 new는 빈 인풋창, edit는 기존에 있는거 쓰는거 인풋창
  >
  >    인풋 value수정, textarea도 괄호사이에 수정 (오픈태그, 클로징태그있으니까) + form 태그를 action으로 update로 보낸다. (method = 'POST')
  >
  >    ⭐ return해서 url로 보낼 때 pk있는거는 article.pk랑 같이 넘겨주는거 중요 ⭐
  >
  > 4. 앱 / urls.py
  >
  >    ```
  >    path('<int:pk>/update/', views.update, name='update'),
  >    ```
  >
  > 5. 앱 / views.py
  >
  >    ```
  >    def update(request, pk):
  >    	article = Article.objects.get(pk=pk)	# 기존꺼 보여줘야함
  >    	article.title = request.POST.get('title')
  >    	article.content = request.POST.get('content')
  >    	artice.save()		# 덮어씌어짐 
  >    
  >    	return redirect('articles:detail', article.pk)
  >    ```
  >
  >    update함수에서 위 form에서 보낸 article 로 덮어씌어준다.
  >
  > 6. 앱 / templates / detail.html
  >
  >    ```
  >    <a href="{% url 'articles:edit' article.pk %}">EDIT</a>
  >    ```
  >
  >    edit 버튼 생성 해서 edit url으로 넘겨준다
  
- **게시글 입력들 forms.py로 해보기**

  > 1. forms.py를 앱 내에 만들기
  >
  >    ```
  >    from django import forms
  >    
  >    class ArticleForm(forms.Form):
  >    	title = forms.CharField(max_length=10)
  >    	content = forms.CharField(widget=forms.Textarea)	# 여러줄들어가는거
  >    ```
  >
  > 2. views.py
  >
  >    new 부분 코드 수정, import 해오기
  >
  >    ```
  >    from .forms import ArticleForm
  >    
  >    def new(reqeust):
  >    	form = ArticleForm()
  >    	context = {
  >    		'form' : form,
  >    	}
  >    	return render(request, 'articles/new.html', context)
  >    ```
  >
  > 3. new.html 수정
  >
  >    forms.as_p 추가
  >
  >    ```
  >    {% extends 'base.html' %}
  >    {% block content %}
  >      <h1 class="text-center">New Article</h1>
  >      <hr>
  >      <form action="{% url 'articles:create' %}" method="POST">
  >        {% csrf_token %}
  >        {{ form.as_p }}
  >        {% comment %} 제목 : <input type="text" name="title"><br>
  >        내용 : <textarea name="content" id="" cols="30" rows="10"></textarea><br> {% endcomment %}
  >        <input type="submit" value="글 작성">
  >      </form>
  >      <a href="{% url 'articles:index' %}">BACK</a>
  >    {% endblock content %}
  >    ```
  >
  >    만약 forms.as_ul 하면 앞에 .이 나타나고 form.as_table 하면 표 안에 항목들이 나열되어 들어감
  >
  > ** 만약 선택지 만들면, 
  >
  > 1. forms.py에 코드 추가
  >
  >    ChoiceField 부분 추가
  >
  >    ```
  >    from django import forms
  >    
  >    class ArticleForm(forms.Form):
  >    	REGIONS = [
  >    		('sl', '서울'),
  >    		('dj', '대전'),
  >    		('gj','광주'),
  >    		('gm', '구미'),
  >    	]
  >    	title = forms.CharField(max_length=10)
  >    	content = forms.CharField(widget=forms.Textarea)
  >    	region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect())
  >    ```
  >
  > ** 만약 model에서 ModelForm을 상속받아 쓴다면, 
  >
  > 1. forms.py
  >
  >    상속을 받고 그 안에 meta 클래스
  >
  >    ```
  >    from django import forms
  >    from .models import Article
  >    
  >    class ArticleForm(forms.ModelForm):		# 상속 받는 것 
  >    
  >    	class Meta:
  >    		model = Article
  >    		fields = '__all__'
  >    		# exclude = ('title', )
  >    
  >    # class ArticleForm(forms.Form):
  >    # 	REGIONS = [
  >    # 		('sl', '서울'),
  >    # 		('dj', '대전'),
  >    # 		('gj','광주'),
  >    # 		('gm', '구미'),
  >    # 	]
  >    # 	title = forms.CharField(max_length=10)
  >    # 	content = forms.CharField(widget=forms.Textarea)	# 여러줄들어가는거
  >    # 	region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect())
  >    ```
  >
  > 2. views.py
  >
  >    ```
  >    def new(request):
  >    	form = ArticleForm()
  >    	context = {
  >    		'form' : form,
  >    	}
  >    	return render(request, 'articles/new.html', context)
  >    
  >    def create(request):
  >    	form = ArticleForm(request.POST)		# titl, content 등 사용자가 입력한거 받아옴
  >    	if form.is_valid():		# 값이 잘 넘어왔는지 확인
  >    		article = form.save()		# form을 저장해서 article 변수에 담음 
  >    	return redirect('articles:detail', article.pk) 
  >    
  >    	# article = Article()
  >    	# article.title = request.POST.get('title')
  >    	# article.content = request.POST.get('content')
  >    	# article.save()
  >    
  >    	# 다른 방법 
  >    	# title = request.POST.get('title')
  >    	# content = request.POST.get('content')
  >    	# article = Article(title=title, content=content)
  >    	# article.save()
  >    	
  >    	# 또 다른 방법
  >    	# title = request.POST.get('title')
  >    	# content = request.POST.get('content')
  >    	# Article.objects.create(title=title, content=content)
  >    ```
  >
  >    유효성 검사 : 입력이 없거나 입력값이 공백이거나 하면 넘어가지 않음 

- **new와 create 하나로 합쳐보기**

  > 1. views.py
  >
  >    else: 하고 new라면 실행할 거 적어줌
  >
  >    ```
  >    def create(request):
  >    	if request.method == 'POST':		# POST로 요청 왔을 떄 실행하고
  >    		form = ArticleForm(request.POST)		# titl, content 등 사용자가 입력한거 받아옴
  >    		if form.is_valid():		# 값이 잘 넘어왔는지 확인
  >    			article = form.save()		# form을 저장해서 article 변수에 담음 
  >    			return redirect('articles:detail', article.pk) 
  >    		return redirect('articles:index')
  >    	else:
  >    		form = ArticleForm()		# context 왜 빠져있는건지 생각해보기
  >    	context = {				
  >    		'form' : form,
  >    	}
  >    	return render(request, 'articles/new.html', context)
  >    
  >    ```
  >
  >    new에서  create로 보낼 때는 method가 post이고
  >
  >    index에서 new할 때는 create로 보내는데 기본 디폴트가 get이니까
  >
  >    views.py에서 new함수가 굳이 없어도 된다는것 (create에서 method 방식에 따라 나눠주면 되니까)
  >
  > 2. index.html
  >
  >    ```
  >    {% extends 'base.html' %}
  >    {% block content %}
  >      <h1 class="text-center">Articles</h1>
  >      <a href="{% url 'articles:create' %}">New</a>
  >      <hr>
  >      <ul> <!--이거 위치가 중요-->
  >        {% for article in articles %}
  >        <li>{{ article.pk }}번 글 - <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></li>
  >      </ul>
  >      {% endfor %}
  >    {% endblock content %}
  >    ```
  >
  >    New의 url경로를 create으로 잡아준다
  >
  > 3. new.html
  >
  >    ```
  >    {% extends 'base.html' %}
  >    {% block content %}
  >      <h1 class="text-center">New Article</h1>
  >      <hr>
  >      <form action="{% url 'articles:create' %}" method="POST"> <!--url안에 '' 로 해도 된다고함-->
  >        {% csrf_token %}
  >        {{ form.as_p }}
  >        {% comment %} 제목 : <input type="text" name="title"><br>
  >        내용 : <textarea name="content" id="" cols="30" rows="10"></textarea><br> {% endcomment %}
  >        <input type="submit" value="글 작성">
  >      </form>
  >      <a href="{% url 'articles:index' %}">BACK</a>
  >    {% endblock content %}
  >    ```
  >
  >    new 에서 form태그의 보내는 url 경로를 create으로 해준다. 어짜피 여기서는 method가 POST이니까 create 함수에서 create 하게 됨
  >
  > ** views.py에서 new 함수 지우려면 urls.py에서 new 의 url도 지워줘야함 + 경로도 create.html로 바꾸고 new.html도 create.html로 바꾼다.
  >
  > ** update와 edit도 하나로 합치기 가능하다 (TIL_G > form 코드 확인)
  
- **bootstrap5 라이브러리 이용**

  > pip install django-bootstrap-v5
  >
  > settings.py > bootstrap5 추가
  >
  > base.html  상단에 load bootstrap5 해주고 안에다가 ```{% bootstrap_css %}  {% bootstrap_javascript %}``` 해줘도 됨.
  >
  > ** load는 각 html 파일마다 해줘야함.

- **프로젝트 > templates에 html 하나 더 만들 때  && 각 html마다 css 적용해줄때**

  > [html 하나 더 만들 때]
  >
  > base.html에 넣고자 하는 곳에 ```{% include 'nav.html' %}``` 하고, 
  >
  > templates > nav.html 만들어준다
  >
  > ```
  > {% load bootstrap5 %}
  > {% load static %}
  > 
  > <!DOCTYPE html>
  > <html lang="en">
  > <head>
  >   <meta charset="UTF-8">
  >   <meta http-equiv="X-UA-Compatible" content="IE=edge">
  >   <meta name="viewport" content="width=device-width, initial-scale=1.0">
  >   {% comment %} <link rel="stylesheet" href="{% static 'articles/css/bootstrap.css' %}"> {% endcomment %}
  >   {% bootstrap_css %}
  >   {% block css %}
  >   {% endblock css %}
  > 
  >   <title>Document</title>
  > </head>
  > <body>
  >   {% include 'nav.html' %}
  >   <div class="container">
  >     {% block content %}
  >     {% endblock %}
  >   </div>
  >   {% comment %} <link rel="stylesheet" href="{% static 'articles/js/bootstrap.bundle.js' %}"> {% endcomment %}
  >   {% bootstrap_javascript %}
  > </body>
  > </html>
  > ```
  >
  > [html마다 css 적용해줄때]
  >
  > 0.settings.py에 static 경로 설정되어있는지 확인
  >
  > ```
  > STATICFILES_DIRS = [
  >     BASE_DIR / 'crud' / 'static',
  > ]
  > ```
  >
  > 1.```{% block css %}``` 적용해준다. 
  >
  > 2.상단에 load static 도 해준다.
  >
  > 3.index.html에서 
  >
  > ```
  > {% load static %}
  > 
  > {% block css %}
  >   <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
  > 
  > {% endblock css %}
  > ```
  >
  > 이 부분 추가한다. 
  >
  > 4.crud>static>stylesheets>style.css 만들어준다

- **modelform 하는 이유**

  > model에서 정의한 스키마와 동일한 데이터를 받고자 한다면, modelform을 상속받아서 쓰면된다

- **forms.py 깔끔하게 하기**

  > ```
  > from django import forms
  > from .models import Article
  > 
  > class ArticleForm(forms.ModelForm):
  > 	title = forms.CharField(
  > 		label = '제목',
  > 		widget = forms.TextInput(
  > 			attrs={
  > 				'class' : 'my-title form-control',
  > 				'placeholder' : '제목을 입력하시오',
  > 				'maxlength' : 10,
  > 			}
  > 		),
  > 		error_messages={
  > 			'required' : '제목 입력 필수',
  > 		}
  > 	)
  > 	content = forms.CharField(
  > 		label = '내용',
  > 		widget = forms.Textarea(
  > 			attrs = {
  > 				'class' : 'my-content form-control',
  > 				'placeholder' : '내용을 입력하시오',
  > 				'rows' : 5,
  > 				'cols' : 30,
  > 			}
  > 		),
  > 		error_messages={
  > 			'required' : '내용 입력 필수',
  > 		}
  > 	)
  > 
  > 	class Meta:
  > 		model = Article
  > 		fields = '__all__'
  > ```
  >
  > 1. error_message를 forms.py에 추가하면 title, content각각 원하는 error message를 넣어줄 수 있음. 이렇게 안하고 create.html에서 form.title.errors라고만 해주면 그냥 둘다 똑같은 에러메시지가 나옴.
  > 2. forms.py에 form.control 넣으면 부트스트랩이 적용되어서 이쁜 모양으로 나옴

- **decorator 추가하기**

  > 1. view.py
  >
  >    ```
  >    from django.views.decorators.http import require_http_methods, require_safe, require_POST
  >    
  >    @require_http_methods(['GET','POST']) 
  >    ```
  >
  >    위와 같이 함.

- **화면에 내가 이미지 넣기**

  > 1. settings.py > STATICFILES_DIRS 추가되어 있는지 확인
  >
  > 2. index.html에
  >
  >    ```
  >    <img src="{% static 'articles/sing.jpg' %}" alt="이미지">
  >    ```
  >
  > 3. articles(앱) > static > articles 폴더 만들고 이 안에 이미지 넣기
  >
  > ** jpg인지 jpeg인지 확인

- **유저가 이미지 업로드 하기**

  > 1. settings.py 
  >
  >    ```
  >    # 입력받은 이미지가 저장될 경로 (이렇게 안하면 그냥 crud에 저장됨)
  >    MEDIA_ROOT = BASE_DIR / 'media'
  >    MEDIA_URL = '/media/'
  >    ```
  >
  > 2. urls.py
  >
  >    ```
  >    from django.conf import settings
  >    from django.conf.urls.static import static
  >    
  >    urlpatterns = [
  >        path('admin/', admin.site.urls),
  >        path('articles/', include('articles.urls')),
  >    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  >    ```
  >
  >    import해주고 static(~) 넣어줘야 한다. 
  >
  > 3. views.py
  >
  >    ```
  >    create, update 함수에
  >    form = ArticleForm(request.POST, request.FILES) 이렇게 한다.
  >    ```
  >
  >    즉, request.FILES 추가
  >
  > 4. models.py
  >
  >    ```
  >    image = models.ImageField(black=True)
  >    ```
  >
  >    추가적으로,
  >
  >    명령어 두개 실행 (models 바뀌었으니까)
  >
  > 5. create.html 또는 update.html에서
  >
  >    ```
  >    <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
  >        {% csrf_token %}
  >        {% bootstrap_form form%}
  >        <input type="submit" value = "submit">
  >    </form>
  >    ```
  >
  >    ```enctype="multipart/form-data"``` 추가해주기
  >
  > 6. detail.html
  >
  >    ```
  >    <img src="{{ article.image.url }}" alt="{{ article.image }}">
  >    ```
  >
  >    디저트 사진 보여져야하니까 
  >
  > ** static, media  차이 : static은 내가 보여주는거고 media는 유저가 올리는 파일인듯

- **Image resize**

  > 1. 명령어
  >
  >    pip install django-imagekit
  >
  >    settings에 imagekit 추가 
  >
  > 2. models.py
  >
  >    ```
  >    image_thumbnail 추가
  >    from import 2줄 복사
  >    ```
  >
  >    processor : 이미지 크기 처리
  >
  >    python manage.py makemigrations 하면 변화사항 없다고 함.
  >
  > 3. image있는 html에서 img src에서 post.image_thumbnail.url로 바꿔준다.
  >
  > 4. 즉, index페이지에서는 썸네일 사진으로 보여주고 deatil에서는 원본 사진으로 보여준다.
  >
  > 5. processimagefield를 복사해서 넣어주면 upload_to는 폴더 경로를 만들어준느것

- **form.html**

  > 1. views.py
  >
  >    return 주소를 form으로 바꿔준다
  >
  > 2. form.html
  >
  >    create와 update로 나눠서 코드 작성

- **404**

  > 1.views.py
  >
  > ```
  > from django.shortcuts import render, redirect, get_object_or_404
  > post = Post.objects.get(pk=pk)
  > 
  > post = get_object_or_404(Post, pk=pk)
  > ```
  >
  > 위 코드를 아래 코드로 바꾼다.



유저에 관련된 앱 만들고 할 때

```
$ python manage.py startapp accounts
settings.py에서 articles밑에 accounts 등록
python manage.py migrate
```

```
프로젝트 > urls.py에 
path('accounts/', include('accounts.urls')),
추가
```

accounts > urls.py 에 

```
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    
]
```

쿠팡에서 장바구니에 넣고 검사 켜서 application > sid를 지워보면 장바구니 탭을 새로고침했을 때 장바구니 안에 물품들이 사라진다.

로그인 만들 때

urls.py

```
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]
```

views.py

```
from django.shortcuts import render
# from django.conrib.auth import 
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):		# 세션을 create
	# get 일때는 login 페이지를 주고,
	# post 일때는 login 을 하면 됨
	if request.method == 'POST':
		pass
	else:
		form = AuthenticationForm()		# 인스턴스 생성
	context = {
		'form' : form,
	}
	return render(request, 'accouts/login.html', context)
```

login.html

```
{% extends 'base.html' %}
{% block content %}
<h1>로그인</h1>
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>

{% endblock content %}



```

여기까지는 로그인 화면 페이지를 보여줌 

이제 session 생성하기 위한 함수 만들어줄것임

views.py

```
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login		# 세션을 create해줌
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):		# 세션을 create
	# get 일때는 login 페이지를 주고,
	# post 일때는 login 을 하면 됨
	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)	# request받은 다음에 데이터받음
		if form.is_valid():
			# 세션 Create
			auth_login(request, form.get_user())
			return redirect('articles:index')

	else:
		form = AuthenticationForm()		# 인스턴스 생성
	context = {
		'form' : form,
	}
	return render(request, 'accounts/login.html', context)

```

base.html

div container안에 이것을 추가

```
<h3>Hello, {{ request.user }}</h3>
```

이렇게 하고 articles/로 들어가면 Hello, admin이 상단에 뜸. 그리고 쿠키에서 session_id를 지우면 Hello, AnonymousUser가 나타남 

로그아웃

base.html

```
	<form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <button class="btn btn-secondary">LOGOUT</button>
    </form>
```

단순 get요청 방식으로 안되게 

urls.py

```
path('logout/', views.logout, name='logout'),
```

views.py

```
from django.contrib.auth import logout as auth_logout
def logout(request):
	if request.method == 'POST':
		auth_logout(request)
	return redirect('articles:index')
```

이거도 method가 POST일때를 조건으로 걸어둬야함

또는

```
from django.views.decorators.http import require_POST
@require_POST
```

이거 넣어서 POST일 때로 제한해줘도 됨

logout은 쿠키에서도 지우고, 데이터베이스에서도 지운다. 두군데에서 지움 ~~!!



cookie 유효기간 설정하기

```
# session cookie의 유효기간 설정
DAY_IN_SECONDS = 86400
SESSION_COOKIE_AGE = DAY_IN_SECONDS
```





로그인 사용자에 대한 접근 제한

2가지 방법

is_authenticated attribute

=> user에 대해서는 항상 True, AnonymousUser에 대해서는 항상 False

base.html

```
<h3>Hello, {{ request.user }}</h3>
    {% if request.user.is_authenticated %}
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <button class="btn btn-secondary">LOGOUT</button>
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">LOGIN</a>
    {% endif %}
    
    
    {% block content %}
    {% endblock %}
```

views.py

이미 로그인을 한 사용자는 로그인 안뜨게 해야함

```
함수 가장 앞에
if request.user.is_authenticated:		# T / F
		# 로그인된 사용자라면
		return redirect('articles:index')
```

index.html

```
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'articles:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  
  <hr>
  {% for article in articles %}
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

두번째 방법

login reuqired decorator

: 사용자가 로그인 했는지 확인하는 view를 위한 데코레이터

로그인 안했으면 create 페이지로 못가고 로그인 페이지로 리다이렉트 된다.

articles > views.py

```
from django.contrib.auth.decorators import login_required
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
```

accounts > login.html

```
{% extends 'base.html' %}
{% block content %}
<h1>로그인</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>

{% endblock content %}
```

accounts > views.py > login 함수

```
def login(request):		# 세션을 create
	# get 일때는 login 페이지를 주고,
	# post 일때는 login 을 하면 됨
	if request.user.is_authenticated:		# T / F
		# 로그인된 사용자라면
		return redirect('articles:index')


	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)	# request받은 다음에 데이터받음
		if form.is_valid():
			# 세션 Create
			auth_login(request, form.get_user())
			return redirect(request.GET.get('next') or 'articles:index')

	else:
		form = AuthenticationForm()		# 인스턴스 생성
	context = {
		'form' : form,
	}
	return render(request, 'accounts/login.html', context)
```

next를 넣어준다



delete를 url로 하고 로그인창이 뜨는데 여기서 로그인하면 에러나는거를 방지

views.py

```
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')
```

authenticated 해줘야함



user의 crud만들기

urls.py

```
path('signup/', views.signup, name='signup'),
```

views.py

```
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signup(request):
	if request.method = 'POST':
		pass
	else:
		form = UserCreationForm()
		context = {
		'form' : form,
	}
	return render(request, 'accounts/signup.html', context)
```

signup.html

```
{% extends 'base.html' %}
{% block content %}
<h1>회원가입</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>

{% endblock content %}

```

비로그인 상태일 때 회원가입 구조가 보여야함

```
<a href="{% url 'accounts:signup' %}">SIGNUP</a>
```

accounts > views.py

```
def signup(request):
	if request.user.is_authenticated:		# T / F
		# 로그인된 사용자라면
		return redirect('articles:index')
		
	if request.method = 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid:
			user = form.save()		# Usercreationform이 성공적으로 끝나면 리턴은 user
			# 회원가입 후 바로 로그인 해주려고
			auth_login(request, user)
			return redirect('articles:index')
	else:
		form = UserCreationForm()
		context = {
		'form' : form,
	}
	return render(request, 'accounts/signup.html', context)
```



user 탈퇴

```
path('delete/', views.delete, name='delete'),


@require_POST
def delete(request):
	if request.user.is_authenticated:
		request.user.delete()
		return redirect('articles:index')
```

base.html

```
{% load bootstrap5 %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% bootstrap_css %}
  <title>Document</title>
</head>
<body>
  <div class="container">
    <h3>Hello, {{ request.user }}</h3>
    {% if request.user.is_authenticated %}
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <button class="btn btn-secondary">LOGOUT</button>
      </form>
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="탈퇴">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">LOGIN</a>
      <a href="{% url 'accounts:signup' %}">SIGNUP</a>
    {% endif %}
    
    
    {% block content %}
    {% endblock %}
  </div>
  {% bootstrap_javascript %}
</body>
</html>
```



update

```
path('update/', views.update, name='update'),

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

```

update.html

```
{% extends 'base.html' %}
{% block content %}
<h1>회원정보수정</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>

{% endblock content %}
```

base.html

```
<div class="container">
    <h3>Hello, {{ request.user }}</h3>
    {% if request.user.is_authenticated %}
      <a href="{% url 'accounts:update' %}">[회원정보수정]</a>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <button class="btn btn-secondary">LOGOUT</button>
      </form>
```

여기에 update 넣음 

accounts > forms.py

```
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

  class Meta:
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name',)
```

accounts > views.py

```
from .forms import CustomUserChangeForm
```

여기까지 하면 이메일, 이름, 성만 수정이 가능하게 됨

accounts > views.py

```
def update(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.asve()
			return redirect('articles:index')
	else:
		form = UserChangeForm()
	context = {
		'form' : form,
	}
	return render(request, 'accounts/update.html', context)
```





** 로그인 로그아웃 이런거 만들때 model이랑 form안건들였어도 migrate해줘야 no such table 오류 안나옴 

-------------------------------------

댓글기능 구현 

댓글 모델은 articles 게시글 폴더의 models.py에 만든다

articles> models.py

```
# 댓글은 articles의 model에 구조 만듬
class Commment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)          # 참조하는 모델의 소문자 넣어준다
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):      # shell_plus에서 댓글이 보이게 하기 위함
        return self.content

```

변경사항이 생겼으므로 makemigrations , migrate하기

shell_plus

```
In [1]: comment = Comment()

In [2]: comment.content = '댓글1'

In [3]: Article.objects.create(title='제목1', cont 
   ...: ent='내용1')
Out[3]: <Article: Article object (2)>

In [4]: Article.objects.all()
Out[4]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>

In [5]: article = Article.objects.get(pk=1)        

In [6]: article
Out[6]: <Article: Article object (1)>

In [7]: comment.article=article

In [8]: comment.article
Out[8]: <Article: Article object (1)>

In [9]: comment.save()

In [10]: comment.pk
Out[10]: 1

In [1]: article = Article.objects.get(pk=1)

In [2]: article
Out[2]: <Article: Article object (1)>

In [3]: article.comment_set.all()
Out[3]: <QuerySet [<Comment: 댓글1>, <Comment: 댁슬2>]>

In [4]: comments = article.comment_set.all()

In [5]: comments
Out[5]: <QuerySet [<Comment: 댓글1>, <Comment: 댁슬2>]>
```

articles>models.py와 forms.py 수정 (댓글부분 추가)

articles > views.py 댓글 함수 추가

articles > detail.html에서 댓글 부분 추가





## 프로젝트 세팅

** models만들고 forms만들고 views 만든다

##### 기본 파일 세팅

- venv
- .gitignore
- readme

```
$ 폴더 만들고 들어와서 vscode열고
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
=> 이거 하면 여기 안에 있는 패키지들 설치해줘 / venv 다시 만들었을 때 사용 
$ pip install django
$ gitignore 파일 만들기 (python,django,window,visualstudio)
$ django-admin startproject crud .
$ pip freeze
=> 버전과 설치된 거 보여줌 
$ pip freeze > requirements.txt
=> 버전, 설치된거 파일 만들어줌
$ python manage.py startapp movies
=> 앱 생성
$ git clone 주소 .
=> 협업시 clone 받아옴 
$ python manage.py dumpdata --indent 4 movies.movie (앱이름.모델이름소문자)
$ python manage.py dumpdata --indent 4 movies.movie > movies.json
=> movies.json을 만들어서 저장해줌 (데이터베이스에 있는 것들을 json파일로 빼준것)
$ movies에 fixtures 폴더 생성 그 안에 movies 생성
=> movies.json을 movies에 넣어줌 (나중에 페어가 받을 수 있게 + 받으면 migrate해줘야해) 
$ python manage.py loaddata movies/movies.json
=> dumpdata한 것을 다시 DB에 저장하는것
$ python manage.py runserver
**db.sqlite를 지운것은 표를 지운것 + 그 안에 데이터도 사라져 => migrate를 다시 해줘야해 // 만약 models.py를 수정하면 makemigrations부터 다시 해야해 // models.py가 스키마를 잡아주는것
$ git remote add origin2 내주소
=> 다른 사람에게 클론 받은걸 내꺼에 올릴때
```

