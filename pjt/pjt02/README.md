# pjt02__Python을 활용한 데이터 수집2



### 느낀점 😳

딕셔너리와 리스트를 잘 다루는 것이 중요함을 다시 느꼈다. 저번 프로젝트부터 연습한 것이라 이번엔  좀 수월하게 할 수 있었는데 대신 URL생성과 KEY를 다루는 부분이 시간이 오래 걸렸다. URL을 만들 때 형식을 꼼꼼하게 보고 그에 맞게 작성해야 오류가 없다는걸 몇번이나 시행착오를 겪었다. SSAFY과정 전에는 이러한 문제를 풀어본 적이 없어서 API를 통해 직접 데이터를 가져올 수 있다는 것이 신기하게 느껴졌다. 



### a.

##### 학습 내용

TMDB 파일에서 URLMaker클래스를 통해 url을 만들고 요청을 보내 응답을 받아오는 과정을 다시 복습할 수 있었다. 특히 OOP 내용에서 배운 부분이 섞여있어  클래스에서 URL 만들고 요청을 보내서 받아오는 과정을 새로 알게 되었다. 

```python
def popular_count():
    
    # tmdb 파일에서 URLMaker클래스에 접근한다. 
    maker = URLMaker('7a8df8004890b70d9d4175ce5a47331d')
    # url을 만들어준다.
    url = maker.get_url()
    # url로 요청을 보내 응답을 받아온다.
    res = requests.get(url)
    # results 키값에 접근하여 value를 가져온다.
    movie_dict = res.json()
    movie_list = movie_dict.get('results')
    # 영화 title들을 담을 리스트를 만든다.
    title_list = []
    # results키값의 value들이 담긴 리스트에서 순회하며 각 요소의 딕셔너리의 title키값의 value를 가져온다. 
    for movie in movie_list:
        title_list.append(movie.get('title'))
    # 영화 타이틀이 담긴 리스트의 길이를 출력해 영화 리스트의 개수를 계산한다. 
    return len(title_list)
```

출력결과

```
20
```



### b. 

##### 학습내용

if문을 사용하여 평점이 8 이상이면 title을 리스트에 추가해주었다. a번과 마찬가지로 url을 만드는 과정을 다시 복습할 수 있었다. 

```python
def vote_average_movies():

    #tmdb 파일에서 URLMaker클래스에 접근한다. 
    maker = URLMaker('7a8df8004890b70d9d4175ce5a47331d')
    # url을 만들어준다.
    url = maker.get_url()
    # url로 요청을 보내 응답을 받아온다.
    res = requests.get(url)
    # results 키값에 접근하여 value를 가져온다.
    movie_dict = res.json()
    movie_list = movie_dict.get('results')
    # 평점이 8이상인 영화들의 목록을 담을 리스트를 만든다.
    vote_list = []
    # movie_list에서 순회하며 각 요소의 딕셔너리의 vote_average 의 value값들을 가져온다. 
    for movie in movie_list:
        # 평점이 8이상이면 리스트에 추가한다. 
        if movie.get('vote_average') >= 8:
            vote_list.append(movie.get('title'))
    # 리스트를 출력한다.
    return vote_list
```

출력결과

```
['Soul', 'Miraculous World: New York, United HeroeZ']
```

### c.

##### 학습내용

풀기 전에 아래처럼 전체 코드를 어떻게 작성할지 아래처럼 생각하고 대강 써놓고 시작했다. 

```
# 불러온 dict형태에서 results부분 부르면 [{},{},{}] 형태이고 여기서 ['평점'] 순서로 sorted 
# sorted(list, key = lambda x : -x['평점'])  ,평점 높은 순서대로
# 여기서 다섯개 꺼내서 리스트에 넣어서 반환
```

정렬을 어떤 방법으로 할지 고민하다가 movie_list에서 람다함수를 사용하여 'vote_average'의 value값 기준으로 내림차순으로 정렬하는 방법을 검색해서 새로 알게 되었다. 어제 공부한 내용이기도 했다. 

```python
vote_avglist = sorted(movie_list, key = lambda x : -x['vote_average'])
```

```python
	#tmdb 파일에서 URLMaker클래스에 접근한다. 
    maker = URLMaker('7a8df8004890b70d9d4175ce5a47331d')
    # url을 만들어준다.
    url = maker.get_url()
    # url로 요청을 보내 응답을 받아온다.
    res = requests.get(url)
    # results 키값에 접근하여 value를 가져온다.
    movie_dict = res.json()
    movie_list = movie_dict.get('results')    
    # 여기까지는 [{'평점' : 34},{'평점' : 34},{'평점' : 34}] 이런형태이다.
    
    # movie_list에서 람다함수를 사용하여 'vote_average'의 value값 기준으로 내림차순으로 정렬하였다.
    vote_avglist = sorted(movie_list, key = lambda x : -x['vote_average'])
    # 영화 다섯개의 정보를 리스트로 반환한다. 
    return vote_avglist[:5]
```

출력결과

```
[{'adult': False,
  'backdrop_path': '/yR27bZPIkNhpGEIP3jKV2EifTgo.jpg',
  'genre_ids': [16, 10751],
  'id': 755812,
  'original_language': 'fr',
  'original_title': 'Miraculous World: New York, United HeroeZ',
  'overview': 'During a school field trip, Ladybug and Cat Noir meet the '
              'American superheroes, whom they have to save from an akumatised '
              'super-villain. They discover that Miraculous exist in the '
              'United States too.',
  'popularity': 1010.305,
  'poster_path': '/kIHgjAkuzvKBnmdstpBOo4AfZah.jpg',
  'release_date': '2020-09-26',
  'title': 'Miraculous World: New York, United HeroeZ',
  'video': False,
  'vote_average': 8.5,
  'vote_count': 326},
 {'adult': False,
  'backdrop_path': '/kf456ZqeC45XTvo6W9pW5clYKfQ.jpg',
  'genre_ids': [10751, 16, 35, 18, 10402, 14],
  'id': 508442,
  'original_language': 'en',
  'original_title': 'Soul',
  'overview': 'Joe Gardner is a middle school teacher with a love for jazz '
              'music. After a successful gig at the Half Note Club, he '
              'suddenly gets into an accident that separates his soul from his '
              'body and is transported to the You Seminar, a center in which '
              'souls develop and gain passions before being transported to a '
              'newborn child. Joe must enlist help from the other '
              'souls-in-training, like 22, a soul who has spent eons in the '
              'You Seminar, in order to get back to Earth.',
  'popularity': 1971.071,
  'poster_path': '/hm58Jw4Lw8OIeECIq5qyPYhAeRJ.jpg',
  'release_date': '2020-12-25',
  'title': 'Soul',
  'video': False,
  'vote_average': 8.3,
  'vote_count': 4234},
  
  ... 생략. 평점순으로 내림차순 정렬된 것을 알 수 있다. 
```



### d. 

##### 학습내용

c번까지는 순탄하게 해결하였는데 d에서부터 url을 생성하면서 시간을 많이 소요하였다. 그리고 처음에 URL을 tmdb에 함수를 새로 만들어서 풀다가 잘못된 것임을 깨달았다.. tmdb는 건들면 안되는 것이었다!

URL만드는 것을 더 주의깊게 봤으면 이렇게 오래 걸리지는 않았을 것 같다. f스트링과 따옴표를 빼먹어서 에러가 자꾸 있었다. URL은 물음표 전까지가 주소, 상세주소이고, 물음표 이후는 딕셔너리와 비슷하게 &로 이어서 작성해야 한다. 

홈페이지에서 API Docs를 보면서 거기서 필요한 정보들을 받아올 수 있는 URL을 만드는 과정이 새롭기도 하고 새로 알게 된 점들이 참 많았다 😊

```python
url = f"https://api.themoviedb.org/3/movie/{reco_id}/recommendations?api_key={my_key}&language=ko"
```

나머지 조건에 맞게 데이터를 뽑아오는 것은 순탄하게 할 수 있었다. 

```python
def recommendation(title):

    # API KEY를 변수에 저장한다. 
    my_key = '7a8df8004890b70d9d4175ce5a47331d'
    #tmdb 파일의 URLMaker클래스에 접근한다. 
    maker = URLMaker(my_key)
    # 영화 제목을 기준으로 TMDB에서 id를 검색한다.
    reco_id = maker.movie_id(title)
    # 이때, 만약 id가 None이라면 None을 반환한다. 
    if reco_id == None:
        return None

    # id를 기준으로 추천영화 목록 조회 URL을 생성한다.
    url = f"https://api.themoviedb.org/3/movie/{reco_id}/recommendations?api_key={my_key}&language=ko"
    # url을 요청하고 응답을 받아오고, dict형태로 바꾼다. 
    res = requests.get(url)
    reco_dict = res.json() 
    # 딕셔너리에서 results 키값에 해당하는 value값들을 가져온다. 
    reco_lists = reco_dict.get('results')
    # 추천받은 영화 제목을 저장할 리스트를 생성한다. 
    reco_list = []
    # reco_lists를 순회하며 title키값에 해당하는 value값들을 가져와 리스트에 넣는다. 
    for reco in reco_lists:
        reco_list.append(reco.get('title'))
    # 추천 영화 제목 list를 반환한다. 
    return reco_list
```

출력결과

```
['원스 어폰 어 타임 인… 할리우드',
 '조조 래빗',    
 '결혼 이야기',  
 '나이브스 아웃',
 '1917',
 '조커',
 '아이리시맨',   
 '미드소마',     
 '라이트하우스', 
 '그린 북',
 '언컷 젬스',
 '어스',
 '더 플랫폼',
 '블랙클랜스맨',
 '포드 V 페라리',
 '더 페이버릿: 여왕의 여자',
 '두 교황',
 '작은 아씨들',
 '테넷',
 '브레이킹 배드 무비: 엘 카미노']
[]
None
```



### e.

##### 학습내용

이 부분에서도 URL 생성하는 부분이 있었다. d에서 만들어봐서 이거는 금방할 수 있었다. 

```python
# id를 기준으로 배우, 감독 목록 조회 URL을 생성한다.
    url = f"https://api.themoviedb.org/3/movie/{credit_id}/credits?api_key={my_key}&language=ko"
```

d와 달랐던 점은 배우와 감독 목록이 담긴 부분을 각각 가져와야한다는 것이었다. 그 안에서 순회하며 조건에 맞는 값들을 리스트에 넣어야 했다. 처음에는 cast로만 만들고 있었는데 나중에 코드 작성하다보니 crew list도 딕셔너리에서 뽑아줘야 함을 알게 되었다!

```python
	# 배우와 감독 목록이 담긴 딕셔너리에서 cast, crew키값에 해당하는 value를 각각 가져온다.
    cast_lists = credit_dict.get('cast')    # [{},{},{}] 이런 형태이다. 
    crew_lists = credit_dict.get('crew')
    # 배우 리스트
    cast_list = []
    # 감독 리스트
    crew_list = []
```

```python
def credits(title):

    # my_key 변수에 API KEY를 넣는다.
    my_key = '7a8df8004890b70d9d4175ce5a47331d'
    #tmdb 파일의 URLMaker클래스에 접근한다. 
    maker = URLMaker(my_key)
    # 영화 제목을 기준으로 TMDB 파일에서 id를 검색한다.
    credit_id = maker.movie_id(title)
    # 만약 아이디가 None이면 None이 반환되게 한다.
    if credit_id == None:
        return None
    # id를 기준으로 배우, 감독 목록 조회 URL을 생성한다.
    url = f"https://api.themoviedb.org/3/movie/{credit_id}/credits?api_key={my_key}&language=ko"
    res = requests.get(url)
    credit_dict = res.json()
    # 배우와 감독 목록이 담긴 딕셔너리에서 cast, crew키값에 해당하는 value를 각각 가져온다.
    cast_lists = credit_dict.get('cast')    # [{},{},{}] 이런 형태이다. 
    crew_lists = credit_dict.get('crew')
    # 배우 리스트
    cast_list = []
    # 감독 리스트
    crew_list = []
    # id가 10이하일 때 리스트에 넣는다.
    for cast in cast_lists:
        if cast.get('cast_id') < 10:
            cast_list.append(cast.get('name'))
    # Directing일 때 리스트에 넣는다.
    for crew in crew_lists:
        if crew.get('department') == 'Directing':
            crew_list.append(crew.get('name'))
    # 딕셔너리를 새로 만들어 위에서 만든 리스트들을 넣는다.
    result = {}
    result['cast'] = cast_list
    result['crew'] = crew_list

    return result
```

출력결과

```
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Chang Hyae-jin'],
 'crew': ['Bong Joon-ho',
          'Han Jin-won',
          'Kim Seong-sik',
          'Lee Jung-hoon',
          'Park Hyun-cheol',
          'Yoon Young-woo']}
None
```



