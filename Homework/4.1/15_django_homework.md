# 15_django_homework

### 1. MTV

```
M : model
응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리한다 (추가, 수정, 삭제한다.)
T : template
파일의 구조나 레이아웃을 정의하고 실제 내용을 보여주는데에 사용한다. 
V : view
HTTP 요청을 수신하고 HTTP 응답을 반환한다. Model을 통해 필요한 데이터에 접근하고 탬플릿에게 응답 서식 설정을 넘긴다. 
```



### 2. 404 Page not found

```
a : articles
b : views
c : views.index
```



### 3. templates and static

```
a : settings.py
b : TEMPLATES
c : STATICFILES_DIRS
```



### 4. migration

```
1) 
python manage.py makemigrations
2)
python manage.py showmigrations
3)
python manage.py sqlmigrate app_name
4)
python manage.py migrate

```



### 5. ModelForm True or False

```
1 F / 동작방식 자체가 다름 (get : 조회느낌 / post: DB조작)
2 T / 
3 F / 약간 확인하는 용도
4 T
```



### 6. media 파일 경로

```
MEDIA_ROOT = BASE_DIR / 'crud' / uploaded_files'
MEDIA_URL = '/uploaded_files/'  -> 정해진건 아닌데 앞뒤로 //있어야함
```



### 7. DB TRUE OR FALSE

```
1 : T
2 : F   :  소문자로 해도 동작은 된다
3 : T
4 : T
5 : F  ??? 
```



### 8. on_delete

```
PROTECT
```



### 9. Like in models

```
a : ManyToManyField
b : related_name
```



### 10 . Follow in models

```
중개 테이블 이름 : accounts_user_followings
id를 제외한 컬럼의 이름 : from_user_id, to_user_id
```























