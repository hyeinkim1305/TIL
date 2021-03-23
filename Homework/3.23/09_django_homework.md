# 09_django_homework

### 1. User Model BooleanField

1) 

```
is_staff, is_active, is_superuser
```



### 2. username max length

```
max_length = 150
```



### 3. login validation

```
is_authenticated
```



### 4. Login 기능 구현

```
(a) AuthenticationForm
(b) login
(c) form.get_user()
```



### 5. who are you?

```
AnonymousUser
```



### 6. 암호화 알고리즘

```python
admin들어가면 나오는 알고리즘 이름을 쓴다!
```



### 7. Logout 기능 구현

```
- logout 함수와 logout 함수의 이름이 동일하다. 따라서 이름을 바꿔주어야한다. 
- method가 POST일 때 실행하도록 제한을 주지 않았다. 따라서 url로 접근해서 로그아웃이 가능해지는 문제가 생긴다. @require_POST decorator를 넣어주어서 해결한다. 
```

