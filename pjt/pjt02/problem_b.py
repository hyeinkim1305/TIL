import requests
from tmdb import URLMaker
from pprint import pprint


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

if __name__ == '__main__':
    pprint(vote_average_movies())    
