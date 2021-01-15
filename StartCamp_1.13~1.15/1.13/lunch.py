import random
menu = ['버거킹', '60계치킨', '파스타맛집']
lunch = random.choice(menu)
print(lunch)


import random
menu = ['버거킹', '60계치킨', '파스타맛집']
phone_book = {'버거킹' : '1234-1234','60계치킨' : '1111-1111','파스타맛집' : '5555-5555'}
lunch = random.choice(menu)    ### lunch에 먼저 랜덤으로 뽑은 메뉴 넣고 나중에 get으로 전화번호 가져오는 거넹
print(lunch)
phone = phone_book.get(lunch)      ### lunch에서 전화번호 가져올 때는 이렇게! 알아두기!
# phone = phone_book[lunch]
print(phone)