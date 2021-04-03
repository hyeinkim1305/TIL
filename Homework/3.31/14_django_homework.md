# 14_django_homework



### 1. M:N True or False

```
1) T
2) T
3) F : related_name은 필수는 아니다 / through와 symmetrical도 가능함 
```



### 2. Like in templates

```django
if request.user in article.like_users.all
```



### 3. Follow in views

```
(a) user_pk
(b) followers ?
(c) filter
(d) remove
(e) add
```

c에서 get을 안쓰는 이유는 없을 때 에러가 생길 수 있으므로!



### 4. User AttributeError

```
User를 Custom해주었기 때문에 signup에서 사용하는 usercreationform을 forms.py에서 재정의해주어 사용해야 한다. 
```

usercreationform같은 것은 modelform이라 db에 변동이 생기기 때문에 재정의해주어야한다. 

### 5. related_name

```
역참조시 호출 방식이 겹칠 수 있기 때문에 related_name을 설정해서 안 겹치도록 해준다. 
```



### 6. follow templates

```
a : person.followings.all
b : person.followers.all
c : request.user
d : person
e : person.pk
```

