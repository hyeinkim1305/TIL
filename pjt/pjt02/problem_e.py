import requests
from tmdb import URLMaker
from pprint import pprint


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

if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None