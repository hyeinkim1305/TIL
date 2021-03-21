
## 3.17 라이브강의때 수정한 부분

##### [초기세팅]
- teminal에서 설치
```
git bash에서 python -m venv venv
vscode열고 
$ pip list
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

##### [create.html]
- form.title / form.content / for field in form 등등 적용
ttle과 content를 떨어뜨려서 각각에 클래스 적용을 위함 

##### [forms.py]
- form-control 추가해줌 
bootstrap적용해서 깔끔하게 해주려고

##### [settings.py] [terminal]
- bootstrap5 설치하고 settings.py에 등록도 함
이후에 template상에서 사용할 때는 load해서 써야해 
$ pip install django-bootstrap-v5
$ pip freeze > requirements.txt

##### [update.html]
- load 추가
```{% load bootstrap5 %}``` 을 extends 밑에 넘어줌
: 라이브러리에 있는 tag, filter 등을 템플릿 상에서 추가적으로 사용할 수 있게 됨
- bootstrap form 추가
```
{% bootstrap_form form %}
    {% buttons %}
        <button type="submit" class="btn btn-primary">Submit</button>
    {% endbuttons %}
```

##### [base.html]
- cdn 대신 다른거 추가, load 추가
:  부트스트랩 cdn처럼 사용 가능한듯

##### [update.html]
- 부트스트랩 라이브러리에 있는 코드들 사용해봄
- include 태그 사용해봄 (템플릿에서 다른 템플릿을 불러올 수 있음)

##### [base.html]
- nav 태그를 넣기 위해 include 이용

##### [nav.html]
- navbar 코드 넣어줌 
: 즉 html 기본 형식은 base.html에 넣어주고, 코드가 길어지거나 복잡한 내용들은 따로 html 만들어서 base.html에 include 해주면 된다

----------
##### [views.py]
- view decorator 적용
```
from django.views.decorators.http import require_safe, require_http_methods
@require_safe
@require_http_methods(['GET', 'POST'])

```