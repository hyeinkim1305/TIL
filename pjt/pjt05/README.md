# pjt05_프레임워크 기반 웹페이지 구현

### 목표

- 데이터를 생성, 조회, 수정, 삭제 할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- Object Relational Mapping에 대한 이해
- Django ModelForm을 활용한 HTML과 사용자 요청 데이터 관리



### 준비사항

- 언어

  > Python 3.8+
  >
  > Django 3.1x

- 도구

  > vsCode
  >
  > Chrome Browser



### 요구사항

커뮤니티 서비스의 게시판 기능 개발을 위한 단계로, 영화 데이터의 CRUD를 하는 로직을 완성한다. 해당 기능은 향후 커뮤니티 서비스의 필수 기능으로 사용된다. 



### 결과화면

![결과화면gif](README.assets/결과화면gif.gif)



### Code

#### pjt05

> .gitignore 생성
>
> requirements.txt 생성

- **settings.py**

  > INSTALLED_APPS에 movies와 bootstrap5등록 (추가로, bootstrap5를 설치)
  >
  > ```'DIRS': [BASE_DIR / 'pjt05' / 'templates',],``` 경로 설정

- **urls.py**

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('movies/', include('movies.urls')),
  ]
  ```

  movies로 오는 url들을 include 한다. 

- **templates > base.html**

  ```django
  {% load bootstrap5 %}
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <title>Document</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'movies:index' %}">INDEX</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movies:create' %}">NEW</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
    <div class="container">
      {% block content %}
      
      
      {% endblock content %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  상단에 bootstrap을 load해서 bootstrap5 라이브러리를 사용한다. 

  각 화면마다 nav바를 만들기 위해 bootstrap에서 navbar코드를 참고해서 넣어준다. 

  bootstrap CDN을 추가한다.

#### movies

- **models.py**

  ```python
  from django.db import models
  
  class Movie(models.Model):
      title = models.CharField(max_length = 100)
      overview = models.TextField()
      poster_path = models.CharField(max_length = 500)
  
      def __str__(self):
          return self.title
  ```

  title, overview, poster_path로 이루어진 스키마를 만들어준다. 

- **forms.py**

  ```python
  from django import forms
  from .models import Movie
  
  class MovieForm(forms.ModelForm):
      class Meta:
          model = Movie
          fields = '__all__'
  ```

  model의 Movie 클래스를 상속받아 form을 만들어준다. 

- **urls.py**

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/update/', views.update, name='update'),
      path('<int:pk>/delete/', views.delete, name='delete'),
  ]
  ```

  각각의 url을 만들어준다. 

- **views.py**

  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from django.views.decorators.http import require_http_methods, require_safe, require_POST
  from .models import Movie
  from .forms import MovieForm
  
  
  @require_safe
  def index(request):
      movies = Movie.objects.order_by('-pk')
      context = {
          'movies' : movies,
      }
      return render(request, 'movies/index.html', context)
  
  @require_http_methods(['GET','POST'])
  def create(request):
      if request.method == "POST":
          form = MovieForm(request.POST)
          if form.is_valid():
              movie = form.save()
              return redirect('movies:detail', movie.pk)
      else:
          form = MovieForm()
      context = {
          'form' : form,
      }
      return render(request, 'movies/form.html', context)
  
  @require_safe
  def detail(request, pk):
      movie = get_object_or_404(Movie, pk=pk)
      context = {
          'movie' : movie,
      }
      return render(request, 'movies/detail.html', context)
  
  @require_POST
  def delete(request, pk):
      movie = get_object_or_404(Movie, pk=pk)
      movie.delete()
      return redirect('movies:index')
  
  @require_http_methods(['GET','POST'])
  def update(request, pk):
      movie = get_object_or_404(Movie, pk=pk)
      if request.method == 'POST':
          form = MovieForm(request.POST, instance=movie)
          if form.is_valid():
              form.save()
              return redirect('movies:detail', movie.pk)
      else:
          form = MovieForm(instance = movie)
      context = {
          'form' : form,
          'movie' : movie,
      }
      return render(request, 'movies/form.html', context)
  
  
  ```

  index 함수의 경우, 저장된 것들을 역순으로 불러와 context에 담아서 넘겨준다. 

  create 함수의 경우, request의 method가 POST일 때와 GET일 때를 구분해주기 위해 if문을 사용한다. 여기서 POST일 경우 저장하라는 의미이므로 저장하고 detail페이지를 보여준다. GET일 경우 새로 form을 만들어서 넘겨준다. 보내는 곳이 form.html인 이유는 update와 create의 html을 하나로 합쳐주었기 때문이다.

  detail 함수는 해당 pk의 영화를 불러와서 detail 페이지로 넘겨준다. 

  delete 함수도 마찬가지로 해당 pk의 영화를 불러와서 삭제하고 홈페이지로 돌아가게 한다.

  update 함수는 GET과 POST일 때를 나눠서 실행하도록 하고, create함수와 다른 점은 pk를 같이 받아와서 수정하려는 해당 영화에 대한 작업을 한다. 따라서 ```instance = movie``` 라는 것이 추가되어있으며, context로 넘겨줄때도 form과 해당 pk영화를 같이 보내준다. 

- **admin.py**

  ```python
  from django.contrib import admin
  from .models import Movie
  
  admin.site.register(Movie)
  ```

  admin을 만들어서 정의한 모델 Movie를 관리자 페이지에서  데이터 생성, 조회, 수정. 삭제가 가능하도록 한다. 

- **templates > index.html**

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1 class="text-center">Movies</h1>
    <hr>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4 g-4">
      {% for movie in movies  %}
        <div class="col">
          <div class="card" style="width: 18rem;">
            <img src="{{ movie.poster_path }}" class="card-img-top" alt="...">
            <div class="card-body d-flex justify-content-center">
              <a href="{% url 'movies:detail' movie.pk %}" class="text-decoration-none text-dark">{{ movie.title }}</a>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
    
  {% endblock content %}
  ```

   for문을 사용하여 view에서 넘겨받은 movies를 순회하여 보여준다.  여기서 grid 개념을 활용하여 가장 작은 화면일 때는 1개씩, 그다음 크기일때는 2개씩, 그 다음 크기일때는 4개씩 보여지도록 한다. img와 title을 각각 넣어준다. 

- **templates > detail.html**

  ```django
  {% extends 'base.html' %}
  {% block content %}
  
    <div class="mt-4">
      <h1 class="text-center">Detail</h1>
    <hr>
    <div class="row">
    <div class="col">
      <p>{{ movie.title }}</p>
      <hr>
      <p>{{ movie.overview }}</p>
    </div>
    <div class="col">
      <img src="{{ movie.poster_path }}" alt="">
    </div>
    </div>
    <div class='d-flex'>
      <div class='me-2'>
      <a href="{% url 'movies:index' %}" class="btn btn-primary">Back</a>
      <a href="{% url 'movies:update' movie.pk %}" class="btn btn-warning">EDIT</a>
      </div>
      <form action="{% url 'movies:delete' movie.pk %}" method="POST">
        {% csrf_token %}
        <button class="btn btn-danger">Delete</button>
      </form>
    </div>
    </div>
   
  {% endblock content %}
  
  ```

  상세 페이지에서도 그리드 개념을 활용하여 title과 overview를 하나의 col로, poster를 하나의 col로 하여 페이지의 반씩을 차지하도록 한다. 그리고 d-flex를 이용하여 EDIT, DELETE, BACK 버튼들을 각각 정렬해준다.
  
- **templates > form.html**

  ```django
  {% extends 'base.html' %}
  {% load bootstrap5 %}
  
  {% block content %}
  
    {% if request.resolver_match.url_name == 'create' %}
      <h1>New</h1>
    {% else %}
      <h1>Update</h1>
    {% endif %}
  
    <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form form layout='horizontal' %}
      {% comment %} {% buttons submit='OK' %}{% endbuttons %}
      {% buttons reset='Cancel' %}{% endbuttons %} {% endcomment %}
      {% buttons %}
          <button type="submit" class="btn btn-primary">OK</button>
      {% endbuttons %}
      {% buttons %}
          <button type="reset" class="btn btn-danger">Cancel</button>
      {% endbuttons %}
    </form>
  
    <a href="{% url 'movies:index' %}" class="btn btn-warning">Back</a>
  
  {% endblock content %}
  ```

  update.html과 create.html을 하나로 합쳐 form.html로 만들어주었다. 만약 create일 때는 New가 상단에 뜨고, update일 때는 Update가 상단에 뜨게 된다. button은 submit일 때와 reset일 때 만들어준다. 

  이 부분을 새롭게 적용해볼 수 있어서 좋았다. 