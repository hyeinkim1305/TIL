### 11_django_pracitce

1)

```sql
In [2]: User.objects.all()
Out[2]: SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>, <User: User object (6)>, <User: User object (7)>, <User: User object (8)>, <User: User object (9)>, <User: User object (10)>, <User: User object (11)>, <User: User object (12)>, <User: User object (13)>, <User: User object (14)>, <User: User object (15)>, <User: User object (16)>, <User: User object (17)>, <User: User object (18)>, <User: User object (19)>, <User: User object (20)>, '...(remaining elements truncated)...']>
```

2) 

```sql
In [4]: User.objects.get(id=19).age
SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 WHERE "users_user"."id" = 19
 LIMIT 21

Execution time: 0.000000s [Database: default]
Out[4]: 26
```

3) 

```sql
In [10]: User.objects.values('age')
Out[10]: SELECT "users_user"."age"
  FROM "users_user"
 LIMIT 21

Execution time: 0.000998s [Database: default]
<QuerySet [{'age': 40}, {'age': 36}, {'age': 37}, {'age': 40}, {'age': 30}, {'age': 26}, {'age': 18}, {'age': 33}, {'age': 23}, {'age': 22}, {'age': 15}, {'age': 22}, {'age': 32}, {'age': 35}, {'age': 24}, {'age': 19}, {'age': 34}, {'age': 17}, {'age': 26}, {'age': 17}, '...(remaining elements truncated)...']>
```

4)

```sql
In [11]: User.objects.filter(age__lte=40).values('id','balance')
Out[11]: SELECT "users_user"."id",
       "users_user"."balance"
  FROM "users_user"
 WHERE "users_user"."age" <= 40
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'id': 1, 'balance': 370}, {'id': 2, 'balance': 5900}, {'id': 3, 'balance': 3100}, {'id': 4, 'balance': 250000}, {'id': 5, 'balance': 220}, {'id': 6, 'balance': 530}, {'id': 7, 'balance': 390}, {'id': 8, 'balance': 3700}, {'id': 9, 'balance': 43000}, {'id': 10, 'balance': 49000}, {'id': 11, 'balance': 640000}, {'id': 12, 'balance': 52000}, {'id': 13, 'balance': 35000}, {'id': 14, 'balance': 720}, {'id': 15, 'balance': 35000}, {'id': 16, 'balance': 720}, {'id': 17, 'balance': 440}, {'id': 18, 'balance': 94000}, {'id': 19, 'balance': 6100}, {'id': 20, 'balance': 590}, '...(remaining elements truncated)...']>
```

5) 

```python
In [12]: User.objects.filter(last_name='김',balance__gte=500).values('first_name')
Out[12]: SELECT "users_user"."first_name"
  FROM "users_user"
 WHERE ("users_user"."balance" >= 500 AND "users_user"."last_name" = '김')
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'first_name': '예진'}, {'first_name': '서현'}, {'first_name': '서영'}, {'first_name': '영일'}, {'first_name': '옥자'}, {'first_name': '광수'}, {'first_name': '성민'}, {'first_name': '정수'}, {'first_name': '서준'}, {'first_name': '은주'}, {'first_name': '미영'}, {'first_name': '우진'}, {'first_name': '순옥'}, {'first_name': '진우'}, {'first_name': '현지'}, {'first_name': '영호'}, {'first_name': '종수'}, {'first_name': '미숙'}, {'first_name': ' 
민재'}, {'first_name': '경자'}]>
```

6) 

```python
In [13]: User.objects.filter(first_name__endswith='수',country='경기도').values('balance')  
Out[13]: SELECT "users_user"."balance"
  FROM "users_user"
 WHERE ("users_user"."country" = '경기도' AND "users_user"."first_name" LIKE '%수' ESCAPE '\')
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'balance': 590}, {'balance': 370}]>
```

7) 

```python
In [14]: from django.db.models import Q
In [16]: User.objects.filter(Q(balance__gte=2000)|Q(age__lte=40)).count()
SELECT COUNT(*) AS "__count"
  FROM "users_user"
 WHERE ("users_user"."balance" >= 2000 OR "users_user"."age" <= 40)

Execution time: 0.000000s [Database: default]
Out[16]: 100
```

8)

```python
In [17]: User.objects.filter(phone__startswith='010').count()
SELECT COUNT(*) AS "__count"
  FROM "users_user"
 WHERE "users_user"."phone" LIKE '010%' ESCAPE '\'

Execution time: 0.000000s [Database: default]
Out[17]: 21
```

9)

```python
In [18]: people = User.objects.get(first_name='옥자',last_name='김')
SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 WHERE ("users_user"."first_name" = '옥자' AND "users_user"."last_name" = '김')
 LIMIT 21

Execution time: 0.000000s [Database: default]

In [19]: people
Out[19]: <User: User object (16)>

In [20]: people.country
Out[20]: '경상남도'

In [21]: people.country = '경기도'

In [22]: people.save()
UPDATE "users_user"
   SET "first_name" = '옥자',
       "last_name" = '김',
       "age" = 19,
       "country" = '경기도',
       "phone" = '011-1038-5964',
       "balance" = 720
 WHERE "users_user"."id" = 16

Execution time: 0.011594s [Database: default]

In [23]: people.country
Out[23]: '경기도'
```

10)

```sql
In [26]: people = User.objects.get(first_name='진호',last_name='백')
SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 WHERE ("users_user"."first_name" = '진호' AND "users_user"."last_name" = '백')
 LIMIT 21

Execution time: 0.000000s [Database: default]

In [27]: people.delete()
DELETE
  FROM "users_user"
 WHERE "users_user"."id" IN (27)

Execution time: 0.002991s [Database: default]
Out[27]: (1, {'users.User': 1})
```

11)

```sql
In [31]: User.objects.order_by('-balance')[:5]
Out[31]: SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 ORDER BY "users_user"."balance" DESC
 LIMIT 5

Execution time: 0.000000s [Database: default]
<QuerySet [<User: User object (70)>, <User: User object (32)>, <User: User object (55)>, <User: User object (73)>, <User: User object (45)>]>
```

12)

```python
In [34]: User.objects.filter(phone__contains='123',age__lt=30)
Out[34]: SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 WHERE ("users_user"."age" < 30 AND "users_user"."phone" LIKE '%123%' ESCAPE '\')
 LIMIT 21

Execution time: 0.000997s [Database: default]
<QuerySet [<User: User object (93)>]>
```

13)

```python
In [35]: User.objects.filter(phone__startswith='010').values('country').distinct()
Out[35]: SELECT DISTINCT "users_user"."country"
  FROM "users_user"
 WHERE "users_user"."phone" LIKE '010%' ESCAPE '\'
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'country': '충청북도'}, {'country': '경상북도'}, {'country': '경기도'}, {'country': '제주특별자치도'}, {'country': '경상남도'}, {'country': '전라남도'}, {'country': '강원도
'}, {'country': '전라북도'}]>
```

14)

```python
In [36]: from django.db.models import Avg

In [37]: User.objects.aggregate(Avg('age'))
SELECT AVG("users_user"."age") AS "age__avg"
  FROM "users_user"

Execution time: 0.000000s [Database: default]
Out[37]: {'age__avg': 28.343434343434343}
```

15)

```python
In [38]: User.objects.filter(last_name='박').aggregate(Avg('balance'))
SELECT AVG("users_user"."balance") AS "balance__avg"
  FROM "users_user"
 WHERE "users_user"."last_name" = '박'

Execution time: 0.000995s [Database: default]
Out[38]: {'balance__avg': 196114.2857142857}
```

16)

```python
In [39]: from django.db.models import Max
In [40]: User.objects.filter(country='경상북도').aggregate(balance=Max('balance'))
SELECT MAX("users_user"."balance") AS "balance"
  FROM "users_user"
 WHERE "users_user"."country" = '경상북도'

Execution time: 0.000000s [Database: default]
Out[40]: {'balance': 400000}
```

17)

```python
In [44]: User.objects.filter(country='제주특별자치도').order_by('-balance')[0].first_name   
SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 WHERE "users_user"."country" = '제주특별자치도'
 ORDER BY "users_user"."balance" DESC
 LIMIT 1

Execution time: 0.001275s [Database: default]
Out[44]: '순옥'
```



