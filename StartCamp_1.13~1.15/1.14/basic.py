number = 3
# print(type(number))


string = '문자열'
# print(type(string))


boolean = True
# print(type(boolean))


string_number = '3'
# print(int(string_number)+5)
# print(string_number+'5')


# f-string
name = '홍길동'
# print(f"{name}입니다.반갑습니다.")


my_list = ['python','java']
# print(my_list[1])
my_list[1] = 'django'
# print(my_list)
print(len(my_list))


foods = ['시리얼','김치찜','초콜릿']
print(foods[2])
foods[2] = '보쌈'
print(foods)


my_home = {
    'location' : 'seoul',
    'mood' : 'sweet'
}
print(my_home['location'])
print(my_home.get('location'))   ### 몰랐던거!!
print(my_home.get('name'))    ### Error를 뽑지 않고 none을 출력한다
my_home['location'] = 'gumi'
# print(my_home)


my_info = {
    'location' : 'cheonan',
    'age' : 25,
    'hobby' : 'drawing'
}
# print(my_info['age'])
# print(my_info.get('location'))


# 기초연산자
# print(3 + 5)
# print(5 - 3)
# print(5 * 3)
# print(5 / 3)
# print(100 // 3)   # 몫을 의미한다
# print( 100 % 3)   # 나머지를 의미
# print(2**5)   # 제곱


# # 비교연산자
# print(5 == 5)   
# # 결과 True
# print(3 == '5')  ### 결과 False
# print( 3 != 5)  
# # 결과 True
# print ( 3>=3) 
# # 결과 True


# 조건문
# n = 9
# if n % 2 == 1:
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')

# if n > 0:
#     print('양수입니다.')
# elif n == 0:
#     print('0입니다')
# else:
#     print('음수입니다.')


# numbers = [1,2,3]
# for number in numbers:
#     print(number)


# 리스트에 홀수 넣어서 출력
numbers = [1,2,3,4,5,6,7,8,9]
ans = []
for number in numbers:
    if number % 2 == 1:
        ans.append(number)
print(ans)

# 홀수만 출력
numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    if i%2 == 1:
        print(i)

# f-string써서 출력
numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    if i%2 == 1:
        print(f'{i}는 홀수입니다.')
