[TOC]

# SQL with django ORM

## 기본 준비 사항

```bash
# 폴더구조
99_sql # only SQL
    hellodb.csv
    tutorial.sqlite3
    users.csv
99_sql_orm # SQL + ORM
    ...
    users.csv # 해당 디렉토리로 다운로드
```

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
  $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```



---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 만 켜고 작성해주세요.



### 1. 기본 CRUD 로직

ORM의 user는 model 클래스이름

1. 모든 user 레코드 조회

   ```python
   # orm
   User.objects.all()
   ```

      ```sql
   -- sql
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(first_name='혜인',
      ...: last_name = '김',
      ...: age=25,
      ...: country='cheonan',
      ...: phone='010-1234-5678',
      ...: balance=500)
   ```

   ```sql
   -- sql
   INSERT INTO users_user VALUES(102,'우중','김',22,'
   천안','010-1212-4545',700);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(pk=101)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE id=101;
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   In [4]: article = User.objects.get(pk=101)
   
   In [7]: article.last_name = '이'
   
   In [9]: article.save()
   
   In [10]: article
   Out[10]: <User: No.101-이혜인>
   ```

      ```sql
   -- sql
   sqlite> UPDATE users_user
      ...> SET first_name = '철수'
      ...> WHERE id=101;
      ```

5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```python
   # orm
   In [11]: article = User.objects.get
In [11]: article = User.objects.get(pk=101)
   
   In [12]: article.delete()
   Out[12]: (1, {'users.User': 1})
   ```
   
   ```sql
   -- sql
   sqlite> DELETE FROM users_user WHERE id=101
      ...> ;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   User.objects.all().count()
   ```

   ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user;
   COUNT(*)
   --------
   101
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   In [14]: User.objects.filter(age=30).values('first_name')       
   Out[14]: <QuerySet [{'first_name': '영환'}, {'first_name': '보람
   '}, {'first_name': '은영'}]>
   ```

      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE age=30;
   first_name
   ----------
   영환
   보람
   은영
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   In [17]: User.objects.filter(age__gte=30).count()
   Out[17]: 43
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age >= 30;
   COUNT(*)
   --------
   43
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   In [18]: User.objects.filter(age__lte=20).count()
   Out[18]: 23
   ```

   ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age <= 20;
   COUNT(*)
   --------
   23
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   In [22]: User.objects.filter(age=30,last_name='김').count()     
   Out[22]: 1
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age=30 and last_name='김';
   COUNT(*)
   --------
   1
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   In[35]:from django.db.models import Q		# 이거 넣어주기!
   In [36]: User.objects.filter(Q(age=30) | Q(last_name='김'))     
   Out[36]: <QuerySet [<User: No.5-차영환>, <User: No.8-김예진>, <User: No.9-김서현>, <User: No.11-김서영>, <User: No.14-김영일>, <User: No.16-김옥자>, <User: No.18-김광수>, <User: No.19-김성민>, <User: No.20-김정수>, <User: No.23-김서준>, <User: No.32-김은주
   >, <User: No.46-김명자>, <User: No.47-김미영>, <User: No.57-안보
   람>, <User: No.60-김은영>, <User: No.62-김우진>, <User: No.70-김
   순옥>, <User: No.78-김진우>, <User: No.82-김현지>, <User: No.85-김영호>, '...(remaining elements truncated)...']>
   ```

   ```sql
   -- sql
   sqlite> SELECT first_name, last_name FROM users_user WHERE age=30 or last_name='김';
   first_name  last_name
   ----------  ---------
   영환          차
   예진          김
   서현          김
   ...
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   In [28]: User.objects.filter(phone__startswith="02-").count()    
   Out[28]: 24
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
   COUNT(*)
   --------
   24
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   n [33]: article = User.objects.filter(country='강원도',last_na 
    ...: me='황')
   
   In [34]: article
   Out[34]: <QuerySet [<User: No.22-황은정>]>
   ```
   
      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE country='강원도'and last_name='황';
   first_name
   ----------
   은정
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   In [38]: User.objects.order_by('-age')[:10]
   Out[38]: <QuerySet [<User: No.1-유정호>, <User: No.4-장미경>, <User: No.28-박성현>, <User: No.53-홍상훈>, <User: No.65-송민서>, 
   <User: No.26-이영식>, <User: No.55-이미경>, <User: No.58-배영일>, <User: No.74-배승민>, <User: No.82-김현지>]>
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
   id  first_name  last_name  age  country  phone          balance
   --  ----------  ---------  ---  -------  -------------  ------- 
   1   정호          유          40   전라북도     016-7280-2855  370
   4   미경          장          40   충청남도     011-9079-4419  250000
   28  성현          박          40   경상남도     011-2884-6546  580000
   53  상훈          홍          40   전라북도     016-7698-6684  550
   65  민서          송          40   경기도      011-9812-5681  51000
   26  영식          이          39   경상북도     016-2645-6128  400000
   55  미경          이          39   경기도      02-6697-3997   890000
   58  영일          배          39   전라남도     010-3486-8085  280000
   74  승민          배          39   강원도      010-4833-9657  840
   82  현지          김          39   충청북도     02-8468-8321   680000
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   In [39]: User.objects.order_by('balance')[:10]
   Out[39]: <QuerySet [<User: No.99-성우진>, <User: No.48- 
   이보람>, <User: No.100-김재현>, <User: No.5-차영환>, <User: No.24-권숙자>, <User: No.61-고우진>, <User: No.92-박
   미경>, <User: No.46-김명자>, <User: No.38-심준호>, <User: No.60-김은영>]>
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY balance LIMIT 10;
   id   first_name  last_name  age  country  phone          balance        
   ---  ----------  ---------  ---  -------  -------------  -------        
   99   우진          성          32   전라북도     010-7636-4368  150     
   48   보람          이          28   강원도      02-2055-4138   210      
   100  재현          김          25   경상북도     016-1252-2316  210     
   5    영환          차          30   충청북도     011-2921-4284  220     
   24   숙자          권          33   경상남도     016-4610-3200  230     
   61   우진          고          15   경상북도     011-3124-1126  300     
   92   미경          박          35   경상북도     010-5203-5705  300     
   46   명자          김          23   전라남도     011-3545-5608  330     
   38   준호          심          28   충청북도     016-6703-7656  340     
   60   은영          김          30   경상북도     02-5110-2334   350 
      ```

3.  잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   In [40]: User.objects.order_by('balance','-age')[:10]   
Out[40]: <QuerySet [<User: No.99-성우진>, <User: No.48- 
   이보람>, <User: No.100-김재현>, <User: No.5-차영환>, <User: No.24-권숙자>, <User: No.92-박미경>, <User: No.61-고
   우진>, <User: No.46-김명자>, <User: No.38-심준호>, <User: No.60-김은영>]>
     ```
   
   ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY balance ASC, age DESC LIMIT 10;
   id   first_name  last_name  age  country  phone          balance       
   ---  ----------  ---------  ---  -------  -------------  -------       
   99   우진          성          32   전라북도     010-7636-4368  150    
   48   보람          이          28   강원도      02-2055-4138   210     
   100  재현          김          25   경상북도     016-1252-2316  210    
   5    영환          차          30   충청북도     011-2921-4284  220     
   24   숙자          권          33   경상남도     016-4610-3200  230     
   92   미경          박          35   경상북도     010-5203-5705  300     
   61   우진          고          15   경상북도     011-3124-1126  300     
   46   명자          김          23   전라남도     011-3545-5608  330     
   38   준호          심          28   충청북도     016-6703-7656  340     
   60   은영          김          30   경상북도     02-5110-2334   350   
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   In [42]: User.objects.order_by('-last_name','-first_nam 
    ...: e')[4]
   Out[42]: <User: No.67-허보람>
   ```
   
      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
   id  first_name  last_name  age  country  phone          balance
   --  ----------  ---------  ---  -------  -------------  -------
   67  보람          허          28   충청북도     016-4392-9432  82000
      ```



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/3.1/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```python
   # orm
   In [43]: from django.db.models import Avg
   In [44]: User.objects.aggregate(Avg('age'))
   Out[44]: {'age__avg': 28.168316831683168}
   ```

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user;
   AVG(age)        
   ----------------
   28.1683168316832
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   In [45]: User.objects.filter(last_name='김').aggregate( 
       ...: Avg('age'))
   Out[45]: {'age__avg': 28.5}
   ```

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user WHERE last_name='김';
   AVG(age)
   --------
   28.5
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   In [46]: User.objects.filter(country='강원도').aggregat 
       ...: e(Avg('balance'))
   Out[46]: {'balance__avg': 157895.0}
   ```

   ```sql
   -- sql
   sqlite> SELECT AVG(balance) FROM users_user WHERE country='강원도';
   AVG(balance)
   ------------
   157895.0
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   In [48]: User.objects.aggregate(balance=Max('balance')) 
       ...: 
   Out[48]: {'balance': 1000000}
   ```

      ```sql
   -- sql
   sqlite> SELECT MAX(balance) FROM users_user;
   MAX(balance)
   ------------
   1000000
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   In [49]: from django.db.models import Sum      

   In [50]: total = User.objects.aggregate(Sum('b 
       ...: alance'))
   
   In [51]: total
   Out[51]: {'balance__sum': 14425740}
   
   In [52]: total['balance__sum']
   Out[52]: 14425740
   ```
   
      ```sql
   -- sql
   sqlite> SELECT SUM(balance) FROM users_user;
   SUM(balance)
   ------------
   14425740
      ```