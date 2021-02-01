import requests
from tmdb import URLMaker



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


if __name__ == '__main__':
    print(popular_count())