import json


def max_revenue(movies):
    
    # 후에 추출할 revenue와 title의 딕셔너리 모음들을 넣을 리스트를 새로 만든다.
    revenue_list = []

    # movies 폴더 안에 많은 json들을 불러온다. 
    for movie in movies:
        movie_id = movie.get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movies_dict = json.load(movie_json)


    return movies_dict
    #     # movies_dict 안에서 revenue와 title을 가져오고 mo dic에 새로 넣는다.
    #     mo = {}
    #     mo["revenue"] = movies_dict.get("revenue")
    #     mo["title"] = movies_dict.get("title")
    #     revenue_list.append(mo)
    
    # # revenue_list에 들어있는 revenue들의 값을 비교하여 가장 큰 title을 찾는다. 
    # # 초기값 설정
    # max_revenue = revenue_list[0]["revenue"]
    # max_movie = revenue_list[0]["title"]

    # # revenue_list에서 하나씩 값을 비교하여 최대값 찾는다.
    # for rev in revenue_list:
    #     if rev.get("revenue") > max_revenue:
    #         max_revenue = rev.get("revenue")

    #         # title값도 같이 도출한다.
    #         max_movie = rev.get("title")

    # return max_movie

 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
