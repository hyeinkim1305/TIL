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