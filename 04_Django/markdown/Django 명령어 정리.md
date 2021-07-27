- **프로젝트 생성 (pjt folder)**
  - django-admin startproject pjt .(pjt와 manage.py 바로 생성)
  - django-admin startproject pjt (pjt와 pjt/manage.py 생성)
     
- **app 생성 (app folder)**
  - python manage.py startapp appname : app 생성
     
- **서버 연결 (web)**
  - python manage.py runserver : 페이지 연결
     
- **버젼 (requirements.txt)**
  - pip freeze > requirements.txt : 버젼 저장
  - pip install -r requirements.txt : 버젼 조회 및 다운로드
     
- **가상환경 (venv folder)**
  - python -m venv venv : 가상환경 폴더 생성
  - source venv/Scripts/activate : 가상환경 실행
  - deactivate : 가상환경 해제
  - pip list : 가상환경 설치된 목록 확인
     
- **설치 (settings.py)**
- pip install django : django 설치
- pip install Pillow : 이미지삽입 (models.py/views.py)
- pip install django-imagekit : 이미지 리사이즈 (settings.py/models.py)
- pip install django-bootstrap-v5 : 부트스트랩 설치 (settings.py)
- pip install django-allauth : 소셜 로그인 설치 (settings.py/urls.py)
- pip install django-debug-toolba
- pip install django-extensions : django-extensions 설치 (settings.py)
- pip install Faker django-extensions : DB 더미데이터
- pip install django-seed : 가짜 데이터 생
- pip install djangorestframework : DRF 설치
- pip install -U drf-yasg : Swagger
- pip install django-bootstrap-pagination : 페이지목록 부트스트랩 (settings.py)
- pip install django-cors-headers : cors-headers 생성 (django와 vuex)
- pip install djangorestframework-jwt : 토큰베이스 아이디 로그인
   
- **관리자 (admin.py)**
  - python manage.py createsuperuser : 관리자 계정 생성
     
- **시험(tests.py)**
  - python manage.py test : 테스트 함수 실행
     
- **DB 동기화 (app/migrations, app/fixtures)**
  - python manage.py makemigrations : migrations 폴더 아래 하위 파일 생성
  - python manage.py migrate : 실행할 때마다 명령어
  - python manage.py dumpdata articles.article > articles.json : fixtures 폴더 아래 articles.json으로 articles.article 정보 생성
  - python manage.py loaddata movies/movie.json : fixtures 폴더 아래 articles/articles.json db에 불러오기
  - python manage.py shell_plus : OOP 입력
  - python manage.py seed articles --number=5 : articles의 앱에 5개의 가짜 데이터 생성
     
- **단축키**
  - Ctrl + [ or ] -> 들여쓰기, 내어쓰기
  - Alt + <방향키> -> 해당 커서에 있는 행 내용을 위아래로 이동
  - Ctrl + Alt + 위/아래 화살표 -> 위아래로 커서를 늘려서 동시에 여러줄 수정할 수 있도록 하는 기능
  - CTRL + D 해당 단어 동시 수정
  - ALT + CLICK 모두 한번에 잡아줘 수정하고싶은 부분들을 한번에 수정
  - ALT + Shift + ↓or↑ 현재 커서가 있는 줄을 복사하여 아래에 붙여넣어준다