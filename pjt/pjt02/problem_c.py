import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    
    #tmdb 파일에서 URLMaker클래스에 접근한다. 
    maker = URLMaker('7a8df8004890b70d9d4175ce5a47331d')
    # url을 만들어준다.
    url = maker.get_url()
    # url로 요청을 보내 응답을 받아온다.
    res = requests.get(url)
    # results 키값에 접근하여 value를 가져온다.
    movie_dict = res.json()
    movie_list = movie_dict.get('results')    # 여기까지는 [{'평점' : 34},{'평점' : 34},{'평점' : 34}] 이런형태이다.
    # movie_list에서 람다함수를 사용하여 'vote_average'의 value값 기준으로 내림차순으로 정렬하였다.
    vote_avglist = sorted(movie_list, key = lambda x : -x['vote_average'])
    # 영화 다섯개의 정보를 리스트로 반환한다. 
    return vote_avglist[:5]
    



if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())