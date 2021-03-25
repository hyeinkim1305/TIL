# 10_django_homework



### 1. Lookup

```
- exact : 정확히 일치
- iexact : 대소문자를 구분하지 않는 정확히 일치
- lt : 보다 작다
```



### 2. 1: N관계설정

```
- PROTECT : 참조된 객체의 삭제를 방지
- SET_NULL : null이 있는 경우 null을 설정한다.
- SET_DFFAULT : foreign key를 기본 값으로 설정한다. 
```



### 3. comment create view

```
commit=False
객체를 만들어 놓고 저장하기 전 단계를 만들어 놓는 것이다. 
```



### 4. 1:N DB API

```
article.comment_set.all
```

