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
