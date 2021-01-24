''' 샘플 영화데이터 중 요구사항 정보만 뽑아 반환하는 함수이다.
    새로운 딕셔너리 Result를 하나 만들고 movie_dict에서 원하는 
    정보를 뽑아 넣어주었다.  '''

import json
from pprint import pprint


def movie_info(movie):
      
    # 0) 결과값 반환을 위한 dict
    result = {}

    # 1) movie_dict에서 원하는 데이터 추출
    id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    # 2) 새로 만든 dict에 key값과 value대응하여 넣어준다.
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