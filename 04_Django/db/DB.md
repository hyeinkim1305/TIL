



```
$ sqlite3 tutorial.sqlite3
SQLite version 3.35.2 2021-03-17 19:07:21
Enter ".help" for usage hints.
sqlite> .databases
main: C:\Users\USER\Desktop\TIL_G\04_Django\db\99_sql\tutorial.sqlite3 r/w
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232
sqlite> .headers on
sqlite> SELECT * FROM examples;
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-2424-1232 
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------      
1   길동          홍          600  충청도      010-2424-1232
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> )
   ...> ;
sqlite> .schema classmates
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
sqlite> CREATE TABLE classmates (
   ...> name TEXT
   ...> age INTEGER
   ...> address TEXT
   ...> )
   ...> ;
sqlite> DROP TABLE classmates;
sqlite> CREATE TABLE classmates (
   ...> name TEXT,
   ...> age INTEGER,
   ...> address TEXT,
   ...> )
   ...> ;
Error: near ")": syntax error
sqlite> CREATE TABLE classmates (
   ...> name TEXT,
   ...> age INTEGER,
   ...> address TEXT);
sqlite> INSERT INTO classmates (
   ...> ;
Error: near ";": syntax error
sqlite> INSERT INTO classmates (name)
   ...> VALUES (홍길동);
Error: no such column: 홍길동
sqlite> INSERT INTO classmates (name)
   ...> VALUES ("홍길동");
sqlite> SELECT * FROM classmates
   ...> ;
name  age  address
----  ---  -------
홍길동
sqlite> INSERT INTO classmates (name, age)
   ...> VALUES ('흥부', 23);
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동
흥부    23
sqlite> INSERT INTO classmates (name, age, address)
   ...> VALUES ('놀부', 28, 'seoul');
sqlite> SELECT * FROM classmates
   ...> ;
name  age  address
----  ---  -------
홍길동
흥부    23
놀부    28   seoul
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동
2      흥부    23
3      놀부    28   seoul
sqlite> DROP TABLE classmates;
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
sqlite> .tables
classmates  examples  
sqlite> .schema classmates
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
sqlite> INSERT INTO classmates(name, age)
   ...> VALUES('홍길동', 30);
Error: NOT NULL constraint failed: classmates.address
sqlite> INSERT INTO classmates VALUES('홍길동', 30, '서울');
Error: table classmates has 4 columns but 3 values were supplied
sqlite> INSERT INTO classmates (name, age, address) VALUES ('길동', 29, '천안');
sqlite> SELECT * FROM classmates;
id  name  age  address
--  ----  ---  -------
1   길동    29   천안
sqlite> INSERT INTO classmates VALUES(2, '혜인', 25, '서울');
sqlite> SELECT * FROM classmates;
id  name  age  address
--  ----  ---  -------
1   길동    29   천안
2   혜인    25   서울
sqlite> INSERT INTO classmates VALUES(2, '혜인', 38, '서울'); 
Error: UNIQUE constraint failed: classmates.id
sqlite> DROP TABLE classmates;
sqlite> CREATE TABLE classmates (
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL);
sqlite> INSERT INTO classmates VALUES('혜인', 25, '천안'),('우중', 22, '천안'),('선희', 49, 
'천안'),('용삼',49,'천안');
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
혜인    25   천안
우중    22   천안
선희    49   천안
용삼    49   천안
sqlite> SELECT rowid, name FROM classmates;
rowid  name
-----  ----
1      혜인
2      우중
3      선희
4      용삼
sqlite> SELECT name FROM classmates;
name
----
혜인
우중
선희
용삼
sqlite> SELECT rowid, name FROM classmates LIMIT 1;
rowid  name
-----  ----
1      혜인
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
rowid  name
-----  ----
3      선희
sqlite> SELECT rowid, name FROM classmates LIMIT 2 OFFSET 3;
rowid  name
-----  ----
4      용삼
sqlite> SELECT rowid, name FROM classmates WHERE address='천안';
rowid  name
-----  ----
1      혜인
2      우중
3      선희
4      용삼
sqlite> SELECT DISTINCT address FROM classmates;
address
-------
천안
sqlite> DELETE FROM classmates WHERE rowid=4;
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
혜인    25   천안
우중    22   천안
선희    49   천안
sqlite> INSERT INTO classmates VALUES ('겨울', 5, '천안');
sqlite> SELECT rowid, * FROM classmates;  
rowid  name  age  address
-----  ----  ---  -------
1      혜인    25   천안
2      우중    22   천안
3      선희    49   천안
4      겨울    5    천안
sqlite> CREATE TABLE tests (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL);
sqlite> INSERT INTO tests(name) VALUES('길동맨');
sqlite> INSERT INTO tests(name) VALUES('호이호이');
sqlite> SELECT * FROM tests;
id  name
--  ----
1   길동맨
2   호이호이
sqlite> DELETE FROM tests WHERE id=2;
sqlite> INSERT test (name) VALUES ('호잇');
Error: near "test": syntax error
sqlite> SELECT * FROM tests;                
id  name
--  ----
1   길동맨
sqlite> INSERT tests (name) VALUES ('호잇');
Error: near "tests": syntax error
sqlite> INSERT INTO  tests(name) VALUES ('호잇');
sqlite> SELECT * FROM tests;                      
id  name
--  ----
1   길동맨
3   호잇
sqlite> UPDATE classmates
   ...> SET name='혜인친구', address='제주도'
   ...> WHERE rowid=3;
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
혜인    25   천안
우중    22   천안
혜인친구  49   제주도
겨울    5    천안
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> SELECT * FROM users WHERE age >= 30;
id,first_name,last_name,age,country,phone,balance
1,"정호","유",40,"전라북도",016-7280-2855,370
2,"경희","이",36,"경상남도",011-9854-5133,5900
...
sqlite> .mode column
sqlite> SELECT * FROM users WHERE age >= 30;
id    first_name  last_name  age  country  phone          balance
----  ----------  ---------  ---  -------  -------------  -------
1     정호          유          40   전라북도     016-7280-2855  370
...
sqlite> SELECT first_name FROM users WHERE age >= 30;  
이름만 주르륵 가져옴
sqlite> SELECT first_name, age FROM users WHERE age >= 30 and last_name='김';
first_name  age
----------  ---
예진          33
영일          35
...
sqlite> SELECT COUNT(*) FROM users;
COUNT(*)
--------
1000
sqlite> SELECT AVG(age) FROM users WHERE age >= 30;                          
AVG(age)        
----------------
35.1763285024155
sqlite> SELECT first_name, MAX(balance) FROM users;
first_name  MAX(balance)
----------  ------------
선영          990000
sqlite> SELECT AVG(balance) FROM users WHERE age >= 30;
AVG(balance)    
----------------
153541.425120773
sqlite> SELECT * FROM users WHERE age LIKE '2_';          
id   first_name  last_name  age  country  phone          balance
---  ----------  ---------  ---  -------  -------------  -------
6    서준          이          26   충청북도     02-8601-7361   530
9    서현          김          23   제주특별자치도  016-6839-1106  43000
...
sqlite> SELECT * FROM users WHERE phone LIKE '02%';
id   first_name  last_name  age  country  phone         balance
---  ----------  ---------  ---  -------  ------------  -------
6    서준          이          26   충청북도     02-8601-7361  530
15   지원          박          24   경상북도     02-3783-1183  35000
...
sqlite> SELECT * FROM users WHERE first_name LIKE '%준';  
id   first_name  last_name  age  country  phone          balance
---  ----------  ---------  ---  -------  -------------  -------
6    서준          이          26   충청북도     02-8601-7361   530
23   서준          김          26   강원도      02-4610-2333   6900
....
sqlite> SELECT first_name FROM users WHERE phone LIKE '%-5114-%'; 
first_name
----------
현준

sqlite> SELECT * FROM users ORDER BY age LIMIT 10;
id   first_name  last_name  age  country  phone          balance
---  ----------  ---------  ---  -------  -------------  -------
11   서영          김          15   제주특별자치도  016-3046-9822  640000
59   지후          엄          15   경상북도     02-6714-5416   16000
61   우진          고          15   경상북도     011-3124-1126  300
125  우진          한          15   강원도      011-8068-4814  3300
144  은영          이          15   전라남도     010-5284-4904  78000
196  지훈          김          15   전라북도     02-9385-7954   760
223  승현          장          15   충청북도     016-5731-8009  450
260  주원          김          15   전라남도     02-4240-8648   6300
294  은정          이          15   경상북도     010-6099-6176  5900
295  정수          강          15   충청북도     02-7245-5623   500

sqlite> SELECT * FROM users ORDER BY age,last_name LIMIT 10;
id   first_name  last_name  age  country  phone          balance
---  ----------  ---------  ---  -------  -------------  -------
295  정수          강          15   충청북도     02-7245-5623   500
61   우진          고          15   경상북도     011-3124-1126  300
998  시우          고          15   제주특별자치도  016-3732-8726  270
791  현숙          곽          15   충청남도     016-7423-1481  710000
11   서영          김          15   제주특별자치도  016-3046-9822  640000
196  지훈          김          15   전라북도     02-9385-7954   760
260  주원          김          15   전라남도     02-4240-8648   6300
315  예준          김          15   충청남도     02-9726-5034   76000
331  예준          김          15   충청북도     016-3898-3279  150000
359  서영          김          15   강원도      010-4016-6803  53000

sqlite> SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
last_name  first_name
---------  ----------
김          선영
나          상현
이          정호
...

sqlite> SELECT last_name, COUNT(*)
   ...> FROM users
   ...> GROUP BY last_name;
last_name  COUNT(*)
---------  --------
강          23
고          10
곽          4
...

sqlite> SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
last_name  name_count
---------  ----------
강          23
고          10
곽          4
...

sqlite> CREATE TABLE articles (
   ...> title TEXT NOT NULL,
   ...> content TEXT NOT NULL
   ...> );
   
sqlite> INSERT INTO articles VALUES ('1번제목','1번내용');

sqlite> ALTER TABLE articles RENAME TO news;

sqlite> .tables				### article이름이 news로 바뀜
classmates  examples    news        tests       users   

sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at TEXT;
   
sqlite> INSERT INTO news
   ...> VALUES ('title','내용',datetime('now'));
```



Data 추가 : INSERT

id 만들 때 autoincrement 넣어서 하면 삭제 후 다시 넣을 때 삭제된거까지 포함된 번호로 들어감. 근데 권장되지는 않음 .

```

USER@LAPTOP-L0LDBJLT MINGW64 ~/Desktop/TIL_G/04_Django/db/99_sql_orm/sql_orm/sql_orm (master)
$ python -m venv venv

USER@LAPTOP-L0LDBJLT MINGW64 ~/Desktop/TIL_G/04_Django/db/99_sql_orm/sql_orm/sql_orm (master)
$ source venv/Scripts/activate
(venv)
USER@LAPTOP-L0LDBJLT MINGW64 ~/Desktop/TIL_G/04_Django/db/99_sql_orm/sql_orm/sql_orm (master)
$ pip list
Package    Version
---------- -------
pip        20.1.1
setuptools 47.1.0
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.      
You should consider upgrading via the 'c:\users\user\desktop\til_g\04_django\db\99_sql_orm\sql_orm\sql_orm\venv\scripts\python.exe -m pip install --upgrade pip' command.   
(venv) 
USER@LAPTOP-L0LDBJLT MINGW64 ~/Desktop/TIL_G/04_Django/db/99_sql_orm/sql_orm/sql_orm (master)
$ pip install -r requirements.txt
Collecting asgiref==3.3.1
  Using cached asgiref-3.3.1-py3-none-any.whl (19 kB)
Collecting backcall==0.2.0
  Using cached backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Collecting beautifulsoup4==4.9.3
  Using cached beautifulsoup4-4.9.3-py3-none-any.whl (115 kB)
Collecting colorama==0.4.4
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting decorator==4.4.2
  Using cached decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Collecting Django==3.1.7
  Using cached Django-3.1.7-py3-none-any.whl (7.8 MB)
Collecting django-bootstrap-v5==1.0.0
  Using cached django_bootstrap_v5-1.0.0-py3-none-any.whl (24 kB)
Collecting django-extensions==3.1.1
  Using cached django_extensions-3.1.1-py3-none-any.whl (222 kB)
Collecting importlib-metadata==2.1.1
  Using cached importlib_metadata-2.1.1-py2.py3-none-any.whl (10 kB)
Collecting ipython==7.21.0
  Using cached ipython-7.21.0-py3-none-any.whl (784 kB)
Collecting ipython-genutils==0.2.0
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting jedi==0.18.0
  Using cached jedi-0.18.0-py2.py3-none-any.whl (1.4 MB)
Collecting parso==0.8.1
  Using cached parso-0.8.1-py2.py3-none-any.whl (93 kB)
Collecting pickleshare==0.7.5
  Using cached pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting prompt-toolkit==3.0.18
  Using cached prompt_toolkit-3.0.18-py3-none-any.whl (367 kB)
Collecting Pygments==2.8.1
  Using cached Pygments-2.8.1-py3-none-any.whl (983 kB)
Collecting pytz==2021.1
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting soupsieve==2.2
  Using cached soupsieve-2.2-py3-none-any.whl (33 kB)
Collecting sqlparse==0.4.1
  Using cached sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting traitlets==5.0.5
  Using cached traitlets-5.0.5-py3-none-any.whl (100 kB)
Collecting wcwidth==0.2.5
  Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting zipp==3.4.1
  Using cached zipp-3.4.1-py3-none-any.whl (5.2 kB)
Requirement already satisfied: setuptools>=18.5 in c:\users\user\desktop\til_g\04_django\db\99_sql_orm\sql_orm\sql_orm\venv\lib\site-packages (from ipython==7.21.0->-r requirements.txt (line 10)) (47.1.0)
Installing collected packages: asgiref, backcall, soupsieve, beautifulsoup4, colorama, decorator, sqlparse, pytz, Django, zipp, importlib-metadata, django-bootstrap-v5, django-extensions, ipython-genutils, traitlets, Pygments, wcwidth, prompt-toolkit, parso, jedi, pickleshare, ipython
Successfully installed Django-3.1.7 Pygments-2.8.1 asgiref-3.3.1 backcall-0.2.0 beautifulsoup4-4.9.3 colorama-0.4.4 decorator-4.4.2 django-bootstrap-v5-1.0.0 django-extensions-3.1.1 importlib-metadata-2.1.1 ipython-7.21.0 ipython-genutils-0.2.0 jedi-0.18.0 parso-0.8.1 pickleshare-0.7.5 prompt-toolkit-3.0.18 pytz-2021.1 soupsieve-2.2 sqlparse-0.4.1 traitlets-5.0.5 wcwidth-0.2.5 zipp-3.4.1
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.      
You should consider upgrading via the 'c:\users\user\desktop\til_g\04_django\db\99_sql_orm\sql_orm\sql_orm\venv\scripts\python.exe -m pip install --upgrade pip' command.   
(venv)
USER@LAPTOP-L0LDBJLT MINGW64 ~/Desktop/TIL_G/04_Django/db/99_sql_orm/sql_orm/sql_orm (master)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying users.0001_initial... OK
(venv)
USER@LAPTOP-L0LDBJLT MINGW64 ~/Desktop/TIL_G/04_Django/db/99_sql_orm/sql_orm/sql_orm (master)
$ sqlite3 db.sqlite3
SQLite version 3.35.2 2021-03-17 19:07:21
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            users_user
auth_user_user_permissions
sqlite> .mode csv
sqlite> .import users.csv users_user
users.csv:1: INSERT failed: datatype mismatch
sqlite> SELECT COUNT(*) FROM users_user;
100
sqlite> .schema users_user;
sqlite> .schema users_user
CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
sqlite> SELECT * FROM users_user;
1,"정호","유",40,"전라북도",016-7280-2855,370
2,"경희","이",36,"경상남도",011-9854-5133,5900
3,"정자","구",37,"전라남도",011-4177-8170,3100
4,"미경","장",40,"충청남도",011-9079-4419,250000
5,"영환","차",30,"충청북도",011-2921-4284,220
6,"서준","이",26,"충청북도",02-8601-7361,530
7,"주원","민",18,"경기도",011-2525-1976,390
8,"예진","김",33,"충청북도",010-5123-9107,3700
9,"서현","김",23,"제주특별자치도",016-6839-1106,43000
10,"서윤","오",22,"충청남도",011-9693-6452,49000
11,"서영","김",15,"제주특별자치도",016-3046-9822,640000
12,"미정","류",22,"충청남도",016-4336-8736,52000
13,"하은","남",32,"전라북도",016-9544-1490,35000
14,"영일","김",35,"전라남도",011-4448-6198,720
15,"지원","박",24,"경상북도",02-3783-1183,35000
16,"옥자","김",19,"경상남도",011-1038-5964,720
17,"병철","고",34,"충청남도",016-2455-8207,440
18,"광수","김",17,"충청북도",016-4058-7601,94000
19,"성민","김",26,"충청남도",011-6897-4723,6100
20,"정수","김",17,"경기도",016-1159-3227,590
21,"동현","신",36,"경상북도",010-1172-2541,4700
22,"은정","황",16,"강원도",016-5956-2725,7000
23,"서준","김",26,"강원도",02-4610-2333,6900
24,"숙자","권",33,"경상남도",016-4610-3200,230
25,"유진","이",24,"경기도",010-2349-9997,270000
26,"영식","이",39,"경상북도",016-2645-6128,400000
27,"진호","백",17,"경상남도",011-3885-5678,18000
28,"성현","박",40,"경상남도",011-2884-6546,580000
29,"준서","서",36,"충청남도",011-8419-5766,44000
30,"영수","박",37,"제주특별자치도",010-1106-3465,35000
31,"시우","이",25,"경상남도",02-6546-9558,460
32,"은주","김",38,"전라북도",016-3075-6557,950000
33,"준영","이",29,"경상남도",010-3950-8990,52000
34,"영자","백",27,"전라북도",02-3971-7686,630000
35,"영길","이",37,"제주특별자치도",016-7770-9292,440000
36,"성훈","양",16,"충청남도",011-2725-8590,6200
37,"예은","이",25,"전라남도",016-8369-3803,4900
38,"준호","심",28,"충청북도",016-6703-7656,340
39,"영미","곽",25,"충청남도",016-8234-1908,450000
40,"유진","문",16,"전라남도",02-6768-7430,6400
41,"정호","백",17,"경상북도",02-7881-7256,570
42,"선영","이",37,"충청북도",011-8272-1305,570000
43,"정남","윤",27,"경상북도",010-9554-7310,270000
44,"예은","남",17,"충청북도",011-2465-6519,8200
45,"중수","이",38,"충청북도",02-3867-9108,780000
46,"명자","김",23,"전라남도",011-3545-5608,330
47,"미영","김",37,"경상남도",02-3446-1832,920
48,"보람","이",28,"강원도",02-2055-4138,210
49,"영길","박",28,"전라북도",02-4179-7716,600
50,"은정","이",17,"전라북도",011-5824-4366,970
51,"영순","지",25,"충청북도",02-6625-4561,5100
52,"준영","윤",35,"강원도",011-4625-3694,95000
53,"상훈","홍",40,"전라북도",016-7698-6684,550
54,"영호","하",16,"강원도",011-8615-2227,6100
55,"미경","이",39,"경기도",02-6697-3997,890000
56,"지민","송",26,"충청북도",010-5065-2165,460
57,"보람","안",30,"제주특별자치도",010-6132-4229,68000
58,"영일","배",39,"전라남도",010-3486-8085,280000
59,"지후","엄",15,"경상북도",02-6714-5416,16000
60,"은영","김",30,"경상북도",02-5110-2334,350
61,"우진","고",15,"경상북도",011-3124-1126,300
62,"우진","김",31,"충청북도",016-3755-6794,8100
63,"도현","장",36,"강원도",02-6003-4829,90000
64,"경희","박",38,"충청북도",02-7842-6750,1900
65,"민서","송",40,"경기도",011-9812-5681,51000
66,"영식","이",25,"전라북도",02-7917-7796,880
67,"보람","허",28,"충청북도",016-4392-9432,82000
68,"광수","최",28,"경상북도",010-8591-9541,9400
69,"건우","배",33,"경상북도",011-1952-5289,300000
70,"순옥","김",24,"제주특별자치도",016-4846-2896,1000000
71,"우진","황",34,"경상북도",011-9734-6132,760
72,"도윤","노",28,"전라남도",011-1162-6129,280000
73,"동현","이",19,"강원도",010-9849-2402,790000
74,"승민","배",39,"강원도",010-4833-9657,840
75,"성수","최",19,"경기도",016-7872-6841,370
76,"성현","윤",20,"전라북도",02-3771-8197,65000
77,"예은","문",38,"강원도",02-2076-3186,880
78,"진우","김",37,"경상북도",02-7295-4461,860
79,"지원","임",24,"경기도",010-1652-1668,2900
80,"예지","황",18,"전라남도",010-7374-4933,9400
81,"명숙","진",26,"강원도",010-6226-1846,690000
82,"현지","김",39,"충청북도",02-8468-8321,680000
83,"도윤","이",22,"경상북도",010-4818-9921,96000
84,"지훈","이",18,"강원도",010-6399-4047,300000
85,"영호","김",33,"강원도",010-7554-1154,63000
86,"종수","김",38,"전라남도",016-6487-9185,73000
87,"미숙","김",19,"전라북도",011-4100-7281,89000
88,"현정","이",26,"강원도",02-9090-4351,160000
89,"성현","신",26,"강원도",011-3292-2801,600
90,"옥자","서",23,"경기도",010-6487-5091,430000
91,"민재","김",39,"경상남도",011-5298-5280,6600
92,"미경","박",35,"경상북도",010-5203-5705,300
93,"하은","손",18,"전라남도",02-9618-1232,4800
94,"순옥","오",28,"경기도",016-9248-5012,420
95,"민재","박",26,"제주특별자치도",011-1808-7167,720000
96,"영미","장",39,"제주특별자치도",016-5533-2063,5100
97,"경자","김",38,"충청남도",016-7677-2212,81000
98,"은경","서",19,"제주특별자치도",011-7368-2620,210000
99,"우진","성",32,"전라북도",010-7636-4368,150
100,"재현","김",25,"경상북도",016-1252-2316,210
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM users_user;
id   first_name  last_name  age  country  phone          balance
---  ----------  ---------  ---  -------  -------------  -------
1    정호          유          40   전라북도     016-7280-2855  370
2    경희          이          36   경상남도     011-9854-5133  5900
3    정자          구          37   전라남도     011-4177-8170  3100
4    미경          장          40   충청남도     011-9079-4419  250000
5    영환          차          30   충청북도     011-2921-4284  220
6    서준          이          26   충청북도     02-8601-7361   530
7    주원          민          18   경기도      011-2525-1976  390
8    예진          김          33   충청북도     010-5123-9107  3700
9    서현          김          23   제주특별자치도  016-6839-1106  43000
10   서윤          오          22   충청남도     011-9693-6452  49000  
11   서영          김          15   제주특별자치도  016-3046-9822  640000
12   미정          류          22   충청남도     016-4336-8736  52000
13   하은          남          32   전라북도     016-9544-1490  35000
14   영일          김          35   전라남도     011-4448-6198  720
15   지원          박          24   경상북도     02-3783-1183   35000
16   옥자          김          19   경상남도     011-1038-5964  720
17   병철          고          34   충청남도     016-2455-8207  440
18   광수          김          17   충청북도     016-4058-7601  94000
19   성민          김          26   충청남도     011-6897-4723  6100
20   정수          김          17   경기도      016-1159-3227  590
21   동현          신          36   경상북도     010-1172-2541  4700
22   은정          황          16   강원도      016-5956-2725  7000
23   서준          김          26   강원도      02-4610-2333   6900
24   숙자          권          33   경상남도     016-4610-3200  230
25   유진          이          24   경기도      010-2349-9997  270000
26   영식          이          39   경상북도     016-2645-6128  400000
27   진호          백          17   경상남도     011-3885-5678  18000
28   성현          박          40   경상남도     011-2884-6546  580000
29   준서          서          36   충청남도     011-8419-5766  44000
30   영수          박          37   제주특별자치도  010-1106-3465  35000
31   시우          이          25   경상남도     02-6546-9558   460
32   은주          김          38   전라북도     016-3075-6557  950000
33   준영          이          29   경상남도     010-3950-8990  52000
34   영자          백          27   전라북도     02-3971-7686   630000
35   영길          이          37   제주특별자치도  016-7770-9292  440000
36   성훈          양          16   충청남도     011-2725-8590  6200
37   예은          이          25   전라남도     016-8369-3803  4900
38   준호          심          28   충청북도     016-6703-7656  340    
39   영미          곽          25   충청남도     016-8234-1908  450000
40   유진          문          16   전라남도     02-6768-7430   6400
41   정호          백          17   경상북도     02-7881-7256   570
42   선영          이          37   충청북도     011-8272-1305  570000
43   정남          윤          27   경상북도     010-9554-7310  270000
44   예은          남          17   충청북도     011-2465-6519  8200
45   중수          이          38   충청북도     02-3867-9108   780000
46   명자          김          23   전라남도     011-3545-5608  330
47   미영          김          37   경상남도     02-3446-1832   920
48   보람          이          28   강원도      02-2055-4138   210
49   영길          박          28   전라북도     02-4179-7716   600
50   은정          이          17   전라북도     011-5824-4366  970
51   영순          지          25   충청북도     02-6625-4561   5100
52   준영          윤          35   강원도      011-4625-3694  95000
53   상훈          홍          40   전라북도     016-7698-6684  550    
54   영호          하          16   강원도      011-8615-2227  6100
55   미경          이          39   경기도      02-6697-3997   890000
56   지민          송          26   충청북도     010-5065-2165  460
57   보람          안          30   제주특별자치도  010-6132-4229  68000
58   영일          배          39   전라남도     010-3486-8085  280000
59   지후          엄          15   경상북도     02-6714-5416   16000
60   은영          김          30   경상북도     02-5110-2334   350
61   우진          고          15   경상북도     011-3124-1126  300
62   우진          김          31   충청북도     016-3755-6794  8100
63   도현          장          36   강원도      02-6003-4829   90000
64   경희          박          38   충청북도     02-7842-6750   1900
65   민서          송          40   경기도      011-9812-5681  51000
66   영식          이          25   전라북도     02-7917-7796   880
67   보람          허          28   충청북도     016-4392-9432  82000  
68   광수          최          28   경상북도     010-8591-9541  9400
69   건우          배          33   경상북도     011-1952-5289  300000
70   순옥          김          24   제주특별자치도  016-4846-2896  1000000
71   우진          황          34   경상북도     011-9734-6132  760
72   도윤          노          28   전라남도     011-1162-6129  280000
73   동현          이          19   강원도      010-9849-2402  790000
74   승민          배          39   강원도      010-4833-9657  840
75   성수          최          19   경기도      016-7872-6841  370
76   성현          윤          20   전라북도     02-3771-8197   65000
77   예은          문          38   강원도      02-2076-3186   880
78   진우          김          37   경상북도     02-7295-4461   860
79   지원          임          24   경기도      010-1652-1668  2900
80   예지          황          18   전라남도     010-7374-4933  9400
81   명숙          진          26   강원도      010-6226-1846  690000
82   현지          김          39   충청북도     02-8468-8321   680000
83   도윤          이          22   경상북도     010-4818-9921  96000
84   지훈          이          18   강원도      010-6399-4047  300000
85   영호          김          33   강원도      010-7554-1154  63000
86   종수          김          38   전라남도     016-6487-9185  73000
87   미숙          김          19   전라북도     011-4100-7281  89000
88   현정          이          26   강원도      02-9090-4351   160000
89   성현          신          26   강원도      011-3292-2801  600
90   옥자          서          23   경기도      010-6487-5091  430000
91   민재          김          39   경상남도     011-5298-5280  6600
92   미경          박          35   경상북도     010-5203-5705  300
93   하은          손          18   전라남도     02-9618-1232   4800
94   순옥          오          28   경기도      016-9248-5012  420
95   민재          박          26   제주특별자치도  011-1808-7167  720000
96   영미          장          39   제주특별자치도  016-5533-2063  5100
97   경자          김          38   충청남도     016-7677-2212  81000
98   은경          서          19   제주특별자치도  011-7368-2620  210000
99   우진          성          32   전라북도     010-7636-4368  150
100  재현          김          25   경상북도     016-1252-2316  210
sqlite>   
```



```

```

```

```

