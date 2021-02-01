import requests
from tmdb import URLMaker
from pprint import pprint


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
    

if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
