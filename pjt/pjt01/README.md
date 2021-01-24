# pjt 01 

### a_answer

```python
import json
from pprint import pprint


def movie_info(movie):
      
    # 결과값 반환을 위한 새로운 dict
    result = {}

    # movie에서 원하는 데이터 추출  # movie_dict에서 뽑는게 아니라 movie에서 뽑는 것이다!
    id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    # 새로 만든 dict에 key값과 value대응하여 넣어준다.
    result['id'] = id
    result['title'] = title
    result['poster_path'] = poster_path
    result['vote_average'] = vote_average
    result['overview'] = overview
    result['genre_ids'] = genre_ids

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```

> output

```
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '      
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```

샘플 영화데이터 중 요구사항 정보만 뽑아 반환하는 함수이다. 새로운 딕셔너리 Result를 하나 만들고 movie_dict에서 원하는 정보를 뽑아 넣어주었다. 오전 라이브 강의 때 설명해주셨던 코드와 유사해 풀이하는데 어려움은 없었다. get을 적극 활용하야겠다. 



### b_answer

```python
import json
from pprint import pprint

def movie_info(movie, genres):

    # genre_ids에 해당하는 genre_names를 genres 리스트에서 찾아 넣고 두 name을 리스트에 더해주었다.
    genre_names = []
    for j in movie.get('genre_ids'):
        for genre in genres:
            if j == genre.get('id'):
                genre_names.append(genre.get('name'))

    # 결과값 반환을 위한 dict
    result = {}

    # movie에서 원하는 데이터 추출
    # 위에서 도출한 genre_names를 genre_ids에 넣어준다.
    id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = genre_names

    # 새로 만든 dict에 key값과 value대응하여 넣어준다.
    # key값은 genre_names 로 설정한다.
    result['id'] = id
    result['title'] = title
    result['poster_path'] = poster_path
    result['vote_average'] = vote_average
    result['overview'] = overview
    result['genre_names'] = genre_ids

    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
    
```

> output

```python
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '      
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```

a에서 원하는 정보만 추출한 딕셔너리를 우선 반영하고 거기서 genre_ids 값을 바꾸어준다. genres_list는 리스트안에 딕셔너리가 여러개 있는 형태임을 주의하였다. 이중 for문을 사용한다는 생각을 빠르게 하지는 못했다. get을 활용하니 훨씬 편하다!



### c_answer

```python
import json
from pprint import pprint


def movie_info(movies, genres):

    # movies안에 여러 movie들에 반복물을 돌려준다.
    mov = []
    for movie in movies:
        
        # genre_ids에 해당하는 genre_names를 genres 리스트에서 찾아 넣고 두 name을 리스트에 더해주었다.
        genre_names = []
        for j in movie.get('genre_ids'):
            for genre in genres:
                if j == genre.get('id'):
                    genre_names.append(genre.get('name'))

        # 결과값 반환을 위한 dict
        result = {}

        # movie_dict에서 원하는 데이터 추출
        id = movie.get('id')
        title = movie.get('title')
        poster_path = movie.get('poster_path')
        vote_average = movie.get('vote_average')
        overview = movie.get('overview')
        genre_ids = genre_names

        # 새로 만든 dict에 key값과 value대응하여 넣어준다.
        result['id'] = id
        result['title'] = title
        result['poster_path'] = poster_path
        result['vote_average'] = vote_average
        result['overview'] = overview
        result['genre_names'] = genre_ids

        mov.append(result)

    return mov

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

```

> output

```python
[{'genre_names': ['Drama', 'Crime'],
  'id': 278,
  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '        
              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '     
              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
  'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
  'title': '쇼생크 탈출',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'Crime'],
  'id': 238,
  'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '    
              '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '   
              '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '       
              '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 '        
              '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 '        
              '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.',
  'poster_path': '/cOwVs8eYA4G9ZQs7hIRSoiZr46Q.jpg',
  'title': '대부',
  'vote_average': 8.7},
 생략 ....
 ..
```

for문을 세개 사용해야 해서 어려웠다. 변수가 너무 많아서 헷갈렸지만 코드 작성하기 전에 어떤 식으로 작성할 지 미리 좀 생각해보고 하니 덜 헷갈렸다. for문들의 위치와 새로운 리스트 혹은 딕셔너리를 만들 때 위치를 잘 잡아야한다는 것을 느꼈다. 안그러면 결과값이 이상해진다.. 



### d_answer

```python
import json

def max_revenue(movies):
    
    # 후에 추출할 revenue와 title의 딕셔너리 모음들을 넣을 리스트를 새로 만든다.
    revenue_list = []

    # movies 폴더 안에 많은 json들을 불러온다. 
    for movie in movies:
        movie_id = movie.get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movies_dict = json.load(movie_json)

        # movies_dict 안에서 revenue와 title을 가져오고 mo dic에 새로 넣는다.
        mo = {}
        mo["revenue"] = movies_dict.get("revenue")
        mo["title"] = movies_dict.get("title")
        revenue_list.append(mo)
    
    # revenue_list에 들어있는 revenue들의 값을 비교하여 가장 큰 title을 찾는다. 
    # 초기값 설정
    max_revenue = revenue_list[0]["revenue"]
    max_movie = revenue_list[0]["title"]

    # revenue_list에서 하나씩 값을 비교하여 최대값 찾는다.
    for rev in revenue_list:
        if rev.get("revenue") > max_revenue:
            max_revenue = rev.get("revenue")

            # title값도 같이 도출한다.
            max_movie = rev.get("title")

    return max_movie

 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

```

> output

```
반지의 제왕: 왕의 귀환
```

revenue와 title을 같이 가져오는 부분이 생각하는데 시간이 걸렸다. 앞선 문제들에서 리스트와 딕셔너리를 많이 써보고 나니 리스트안에 각각 딕셔너리들로 넣어야겠다고 생각해서 풀었다. 그리고 최대값 찾는 것은 평소 자주 사용하던 max함수가 아닌 수업 시간에 배웠던 풀이방식을 적용해 풀어보았다. 

중간 중간 오타, 에러와의 전쟁이었다.. 





### e_answer

```python
import json

def dec_movies(movies):

    release_list = []
    titles = []

    # d번의 코드를 이용한다.
    for movie in movies:
        movie_id = movie.get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movies_dict = json.load(movie_json)

        # movies_dict 안에서 revenue와 title을 가져오고 mo dic에 새로 넣는다.
        mo = {}
        mo["release_date"] = movies_dict.get("release_date")
        mo["title"] = movies_dict.get("title")
        release_list.append(mo)

    # release_list안에 각 rel들의 release date 값들의 [5:7] 슬라이싱값을 12와 비교한다.
    for rel in release_list:
        if (rel.get("release_date"))[5:7] == '12':
            
            # 12와 같다면 titles에 붙인다.
            titles.append(rel.get("title"))
    
    return titles


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
```

> output

```
['그린 마일', '인생은 아름다워', '반지의 제왕: 왕의 귀환', '스파이더맨: 뉴 유니버스']
```

d와 비슷한 방식으로 풀고 12월인지 확인하는 부분을 새로 코드작성하였다. 12와 어떻게 비교하면 좋을지 고민하다가 키값으로 release date에 접근한 후 슬라이싱으로 잘라 비교하는 방법을 적용하였다. 덕분에 d에서 새로 만든 mo dict 코드가 여기서도 유사하게 적용되었다. 



전반적으로 리스트와 딕셔너리를 잘 다루어야겠다는 생각이 들었다. 스타트캠프때와 유사한 문제였지만 그때보다는 어렵게 느껴졌고 전체 문제들 중에서 b번에서 가장 시간 소요가 컸다. b번에서 이중 for문으로 id를 name으로 바꾸는 과정이 좀 어렵게 느껴졌고 여러가지 방법을 해보다 풀게 되었다. 리스트에 name값들을 추가해서 본래 딕셔너리에 넣어주는 방식을 앞으로 종종 다시 복습해봐야겠다. 

리드미를 작성하는데에도 시간이 꽤 걸려 앞으로는 문제 각각 풀면서 작성해야겠다.. 이모지 넣는거는 잘 안된다ㅜㅜ