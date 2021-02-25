# 다시볼거

- str안에서는 remove 못 쓴다!!

- list('234') 이렇게 하면 ['2','3','4'] 이렇게 나온다.



----------------------

### 교재 00



```
Containment Test
in 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있습니다.

'a' in 'apple'
True

1 in [1,2,3]
True
```



```
단축평가
파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.
파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.
and 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환된다.
or 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환한다.

'a' and 'b'
'b'

'a' or 'b'
'a'

vowels = 'aeiou'
('a' and 'b') in vowels  
False
('b' and 'a') in vowels
True

# and : 둘다 True여야 True
# 첫번째 True, 두 번째 것도 확인해야함
print(3 and 5)   # 3이True니까 5까지 검사해서 출력이 5가 된 것
print(3 and 0)
print(0 and 3)  # 이미 False가 나왔으니까 3까지 확인할 필요는 없으니까 0이 나옴
print(0 and 0)
5
0
0
0

print(3 or 5)   
print(3 or 0)
print(0 or 3)   # 0은 False이다. # True인거 확인해야해서 3까지 간 것 
print(0 or 0)
3
3
3
0
```



```
positive_num = 4
print(-positive_num)

negative_num = -4
print(+negative_num)
print(-negative_num)

-4
-4
4
```



```
암시적 형변환은 파이썬 내부적으로 자동으로 형변환하는 경우
bool, numbers(int,float,complex)

True + 5    # True는 integer로 바꿨을 때 1이다.
6

result = int_number + float_number
print(result, type(result))
# int와 float을 더하면 float이다.

result = int_number + complex_number
print(result, type(result))
# int와 complex를 더하면 complex이다.

a = '3.5'  # 3.5리는 문자열은 float으로만 변환 가능
int(a) # 에러

# float 3.5는 int로 변환이 가능합니다.
a = 3.5
int(a) # 뒤에 자리는 버림하는듯
3

## 즉 모든거는 문자열로 표현이 가능하고, float는 int로 변환 가능
```



```
0, 0.0, (), [], {}, '', None     :  False
```

```
bool('0')
True

bool(0)
False

bool(0.1)
True
```





```
import datetime
today = datetime.datetime.now()
print(today)

2021-01-18 10:28:01.974583
```

```
f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'

'오늘은 21년 01월 18일 Monday'
```

```
pi = 3.141592
f'원주율은 {pi:.4}! 반지름이 2일때 원의 넓이는 {pi*2*2}'   
# 소수점 넷째자리에서 반올림

'원주율은 3.142! 반지름이 2일때 원의 넓이는 12.566368'
```



```
print('Hello, {}. 내 성적은 {}'.format(name,score))
```

```
print(f'Hello, {name}. 내 성적은 {score}. {score}지롱!')
```

```
name = 'Kim'
score = 4.5
print('Hello, %s' % name)   # string
print('내 성적은 %d' % score)  # 정수 # 내림으로 하는 듯
print('내 성적은 %f' % score)  # 실수

Hello, Kim
내 성적은 4
내 성적은 4.500000
```



```python
print('개행 문자 말고도 가능합니다', end='!')
print('진짜로', end='!')
print('알고보면 print는 기본이 \\n', end='!')

개행 문자 말고도 가능합니다!진짜로!알고보면 print는 기본이 \n!
```



```
print('내용을 띄워서 출력하고 싶으면?', end='\t')
print('옆으로 띄워짐')

내용을 띄워서 출력하고 싶으면?	옆으로 띄워짐
```



```
\n	줄 바꿈
\t	탭
\r	캐리지리턴
\0	널(Null)
\\	\
\'	단일인용부호(')
\"	이중인용부호(")

```

```
a = 3.5 - 3.12
b = 0.38

abs(a-b) <= 1e-10
결과값
True
```



```
round는 round(n,2)이면 소수점 둘째자리까지 나타냄
```



```python
import keyword
print(keyword.kwlist)
# 사용불가한 키워드들이 나옴
```

```
0o  :  8진수
0b  :  2진수
0x  :  16진수
```

```python
pi = 314e-2
print(pi,type(pi))
```

> output

```
3.14 <class 'float'>
```



```python
x,y =10,10
print(x,y)
```

> output

```
10 10
```



```python
lunch = [
    '짜장면', '짬뽕', '탕수육',
    '군만두', '물만두', '왕만두',
]
print(lunch)
```

> output

```
['짜장면', '짬뽕', '탕수육', '군만두', '물만두', '왕만두']
```



```python
print("""hello
world""")
```

> output

```
hello
world
```





---------------

### 중간 체크



```
# 주의할점 : 리스트형태를 int로 바꾸는 거를 했음 ! 이러지 말기
# 문자열에서도 리스트처럼 할 수 있는거 상기하기!
```

```
즉 
input().split()  은 리스트로 형변환 됨
map(int,input().split()) 은 리스트로 형변환 안돼 대신
list(map(int,input().split())) 은 리스트로 변환됨!
```



```python
# input중 최대값 출력하는 것인듯

T = int(input())
for tc in range(T):
    max_val = 0
    numbers = input().split()  # input().split()은 공백으로 입력받아서 리스트로 변환(str형태)
    # numbers = map(int,input().split()) 하면 int형으로 다 받음 근데 리스트로 변환은 안돼
    for idx, number in enumerate(numbers):
        if idx == 0:
            max_val = int(number)
        else:
            if int(number) > max_val:
                max_val = int(number)
	print(max_val)

```



```
a = [[1,2],[3,7],[4,8]]
for i in a:
    print(i[0])
```

> output

```
1
3
4
```



```
a = [[1,2],[3,7],[4,8]]
for i in a:
    print(i)
```

> output

```
[1, 2]
[3, 7]
[4, 8]
```



```
*** 즉, 키워드인자, 기본인자는 가장 마지막에!!

기본인자 : name = '혜인' 

기본인자값을 가지는 인자 다음에 기본 값이 없는 인자는 올 수 없음.
무조건 기본 인자값을 가지는 인자는 마지막에

키워드인자는 함수호출시 사용, 직접 변수의 이름으로 특정 인자 전달 가능
키워드 인자 다음에 위치 인자 불가 / 그냥 특정인자 전달하는거는 다음에 특정인자 없는거 못온다는 것 / 

def greeting(age, name = 'john'):
    return f'{name}은 {age}살입니다.'
greeting(name = '철수', age = 24)   # 가능
greeting(24)                                      # 가능 
greeting(age=24, '철수')                  # 불가 # 키워드 인자 다음에 위치 인자 불가

------
기본값
가변인자 f(3,5)   : 투플로 관리
가변 키워드 인자 f(a=3, b=5)  : 키워드 밸류 이렇게 관리

# 가변인자
def func(a, b, *args):
# *args는 임이의 개수의 위치 인자, 매개변수 목록의 가장 마지막
def students(*args,prof):
    for student in args:
        print(student)
    print(f'존경하는 교수님 {prof}')

students('희은','태영',prof = '탁희')   # 가능

def students(prof,*args):
    for student in args:
        print(student)
    print(f'존경하는 교수님 {prof}')

students('교수','태영','희은')   # 가능

# 가변 키워드 인자
def func(**kwargs):      # **kwargs   :  임의의 개수의 키워드 인자를 받음을 의미


```



```
numbers = range(1,21)
count = 0
for number in numbers:
    # 1은 boolean True
    # 0은 boolean False
    if number % 2 :
        count += 1
print(count)
```

```
sep은  사이사이

end는 끝에
```

```
print(1,2,3,sep = "\n")  
출력값이 줄 넘김 되서 나온다
sep 파라미터 : print 함수에서 출력할 값이 여러 개일때 각 값의 사이사이에 삽입할 문자를 지정할 수 있는 파라미터

end = ' ' 는 공백 하나씩 띄어서 출력

import random
menu = ['라면','파스타','떡국','가지조림']
choice = random.choice(menu)
print(choice)
sample = random.sample(menu,3)
print(sample)

range(5,0,-1)일때 5 4 3 2 1 나옴
```

```
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 아래에 코드를 작성하시오.

print(students.count('이영희'))

# sol2
# vote = 0
# for i in students:
#     if i == '이영희':
#         vote += 1
        
# print(vote)
```

```
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.

print(max(numbers))
# sol2
# n = 0
# max_number = numbers[0]
# for i in range(len(numbers)):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
# print(max_number)
```



## 'a'가 싫어


> 입력으로 짧은 영단어 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과를 출력하시오.

```
word = input()

#아래에 코드를 작성하시오.

# word_edit = word.replace('a','')
# print(word_edit)

for i in word:
    if i != 'a':
        print(i, end='')
```

for i in word이런거는 문자열이랑 리스트에서 된당~



## 단어 뒤집기

> 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

```
word = input()

# 아래에 코드를 작성하시오.

print(''.join(reversed(word)))

# sol2
# output = ""
# for i in word:
#     output = i + output 
# print(output)

#sol3
print(word[::-1])   # 알아두기!!
```



## 가로로 출력하기

> 자연수 number를 입력 받아, 1부터 number까지의 수를 가로로 한칸씩 띄어 출력하시오.

```
number = int(input())

# 아래에 코드를 작성하시오.

for i in range(1,number+1):
    print(i,end=' ')
```



##  네모 출력

> 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(`*`) 문자를 이용하여 출력하시오. 단, 반복문은 사용할 수 없다.

```
n = 5
m = 9
print(('*'*n + '\n') * m)
# print((('*'*n + '\n') * m)[:-1])   # 이렇게 하면 마지막 개행문자는 삭제됌.
```



```range(5,0,-1)일 때 54321 나온다 !

```

-----------------------------------------

### H.W

```python
def my_all(elements):
    if len(elements) == 0:
        return True
    
    for element in elements:
        if bool(element) == False:
            return False
            break
        return True

# sol2
def my_all(elements):     # []는 리스트 안에 아무것도 없으니까 애초에 for문 돌지 않음
    result = True
    for e in elements:
        if bool(e) == False:
            result = False
            break
    return result

# sol3
def my_all(elements):
    result = True
    for element in elements:
        # element가 False이면 if not element가 True가 되니까 실행
        if not element:
            result = False
            break
    return result

# sol4
def my_all(elements):
    for element in elements:
        if not element:
            return False
    return True
#[]가 True가 되는 이유는 element가 없으니까 if문을 갈 일이 없고 결국 True가 리턴

```

```
print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))
출력결과
True
True
True
True True False
```



```
def sum_of_digit(number):
    result = 0
    for num in str(number):
        result += int(num)
    return result

# 재귀로 풀기
def sum_of_digit(number):
    if number > 0:
        v = number % 10
        number = number // 10
        return v + sum_of_digit(number)
    else:
        return number

# sol2
def sum_of_digit(number):
    total = 0
    while number:    # 즉 number가 있으면 실행되는 것, number = 0이면 False라 작동안됨
        total += number % 10
        number = number // 10
    return total
    
# sol3 재귀로 풀기
# base case가 있어야함.
def sum_of_digit(number):
    if number < 10:
        return number
    else:
        remainder= number % 10
        number //= 10
        return sum_of_digit(number) + remainder

```

```
print(sum_of_digit(1234))
print(sum_of_digit(4321))
10
10
```



```python
def is_pal_recursive(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    return is_pal_recursive(word[1:-1])


# sol 2
def is_pal_recursive(word):
    if len(word) < 2:
        return True
    else:
        if word[0] == word[-1]:
            word = word[1:-1]
            return is_pal_recursive(word)
        else:
            return False

# sol 3
def is_pal_recursive(word):
    if len(word) < 2:
        return True
    
    if word[0] == word[-1]:
        word = word[1:-1]
        return is_pal_recursive(word)
    else:
        return False
    
# sol 4
def is_pal_recursive(word):
    
    if len(word) > 1:
        if word[0] == word[-1]:
            return is_pal_recursive(word[1:-1])
        else:
            return False
            
    else:
        return True
```

```python
print(is_pal_recursive('tomato'))
print(is_pal_recursive('racecar'))
print(is_pal_recursive('azza'))
False
True
True
```

```
장점은 변수사용이 줄어든다.
단점은 메모리 공간이 쌓이거나 속도가 늘어진다. 
```



```python
def get_strong_word(a,b):
    a_sum = 0
    b_sum = 0
    for i in a:
        a_sum += ord(i)
    for j in b:
        b_sum += ord(j)
        
    if a_sum > b_sum:
        return a
    elif a_sum < b_sum:
        return b
        
get_strong_word('tom','john')
결과값
'john'
```

```
for i in range(2,10):
    print(f'--{i}단--')
    for j in range(1,10):
        print(f'{i} x {j} = {i * j}')
```

```
word = input()
for i in word:
    if i != 'a':
        print(i, end='')
출력결과
apple
pple
```

```
# 소수 판별
# sol2  # else 위치 주의
for num in range(2, number):
    if number % num == 0:
        print('N')
        break            # for문이 끝나는 것 ,. 반복 종료
else:                    # for문의 세트인 것 / if랑 같은 라인에 넣으면 Y가 여러개 나온다. 약수들마다 나오게됌
    print('Y')           # 소수는 그럼 for문 다 돌아보고 break가 안걸릴 때 Y가 나오는 것 

```

```
# 아래에 코드를 작성하시오.
ans = []
for i in range(1,51):
    ans.append(i)
    answer = ans[::2]     # 두 개씩 건너뜨어서 나온다
print(answer)

```

>  output

```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
```

-----------

### 교재 01

* 함수를 구현할 때는 함수 안에 있는 매개변수 기준으로 짜는 것이다! 프로젝트에서 틀림!

비시퀀스형 : set, 딕셔너리

```
word[:]
# 이거는 문자 전체 나오는 슬라이싱기호이다

print(my_tuple[0])
# 튜플은 읽을 수 있다

print('안녕,' + '하세요')
print((1, 2) + (5, 6))
print([1,2] + [5,6])
안녕,하세요
(1, 2, 5, 6)
[1, 2, 5, 6]

my_list = [0,0,0,0,0,0]
my_list = [0]*6
# 숫자 0이 6개 있는 list

num_list[0::3]
# 0부터 끝까지 3씩 건너뛰어서 리스트

set은 중괄호{}를 통해 만들며, 순서가 없고 중복된 값이 없다

# 합집합
set_a | set_b

# 교집합
set_a & set_b

int(3.5) : 3
int('3.5') : error

container 중에 
string, list, tuple, range : 시퀀스
set, dict : 시퀀스 아님
string, tuple, range는 변경 불가능
```



### 교재 02

```python
enumerate : 인덱스와 값을 함께 활용 가능
>>> t = [1, 5, 7, 33, 39, 52]
>>> for p in enumerate(t):
...     print(p)
... 
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
>>> for i, v in enumerate(t):
...     print("index : {}, value: {}".format(i,v))
... 
index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52

```

```python
break : 반복문 종료 for문, while문
continue : continue 이후의 코드를 수행하지 않고 다음 요소부터 계속하여 반복수행한다.

for i in range(6):
    if i % 2 == 0:
        continue
        # continue 이후의 코드는 실행되지 않습니다.
    print(f'{i}는 홀수다.')

출력결과
1는 홀수다.
3는 홀수다.
5는 홀수다.
```

```python
for i in range(3):
    print(i)
    if i == 100:
        print(f'{i}에서 break 실행됌.')
        break
else:
    print("break 실행안됌.")
    
# for문을 다 빠져나오면 else에 있는거 실행함
# 출력결과
0
1
2
break 실행안됌.
-----------------------------------------------------------------------
for i in range(3):
    print(i)
    if i == 1:
        print(f'{i}에서 break 시행됌.')
        break
else:
    print('break 시행안됌.')

출력결과
0
1
1에서 break 시행됌.
```

```python
# pass
for i in range(5):
    if i == 3:
        pass
    print(i)
출력결과
0
1
2
3
4
-------------------------------------------------------------------------
# continue
for i in range(5):
    if i == 3:
        continue
    print(i)
출력결과
0
1
2
4
```



### 교재 03

```
* 함수는 `매개변수(parameter)`를 넘겨줄 수도 있다.

* 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있다. (`return` 값이 없으면, `None`을 반환한다.)

* 오직 하나 반환
* 만약, return이 없으면 => none을 반환
* 만약, 여러개를 , 로 이어서 리턴하면 => tuple로 묶어버린다.
```

```
a.sort()는 원본을 바꿔버리고, return이 값이 없음
sorted(a) : 원본은 노터치
```

```
매개변수 : 함수 내부에서 활용할 변수
전달인자 : 함수를 호출하는 부분 혹은 실제 전달되는 입력값
```

```
def my_sum(a,b=0):
    return a + b
my_sum(3)
출력결과
3

def my_sum(a=0,b):    # 기본인자값 이거는 안됀다. 아래 예시 같이 보기
    return a + b
my_sum(5)
출력결과
에러

** 기본 인자값은 마지막에만 사용 가능!
```

```
정리
기본인자값을 가지는 인자 다음에 기본 값이 없는 인자는 올 수 없음. 무조건 기본 인자값을 가지는 인자는 마지막에

키워드인자는 함수호출시 사용, 직접 변수의 이름으로 특정 인자 전달 가능 키워드 인자 다음에 위치 인자 불가 / 그냥 특정인자 전달하는거는 다음에 특정인자 없는거 못온다는 것 /
```

##### 가변(임의) 인자 리스트(Arbitrary Argument Lists)

앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트`*args`를 활용합니다. 

가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다. 

---

**활용법**

```python
def func(a, b, *args):
```
> `*args` : 임의의 개수의 위치인자를 받음을 의미
>
> 보통, 이 가변 인자 리스트는 매개변수 목록의 마지막에 옵니다.

```
# 기본값
# 가변인자 f(3,5)   : 투플로 관리
# 가변 키워드 인자 f(a=3, b=5)  : 키워드 밸류 이렇게 관리

```

```
def students(*args,prof):
    for student in args:
        print(student)
    print(f'존경하는 교수님 {prof}')
students('희은','태영','탁희')  # error
students('희은','태영',prof = '탁희')   
# 출력결과
희은
태영
존경하는 교수님 탁희
------------------------------------------------------------------------
def students(prof,*args):
    for student in args:
        print(student)
    print(f'존경하는 교수님 {prof}')
students('교수','태영','희은') 
# 출력결과
태영
희은
존경하는 교수님 교수
```

```
def my_max(*args):
    result = 0
    for idx,val in enumerate(args):
        if idx == 0:
            result = val
        else:
            if val > result:
                result = val
    return result
my_max(-1, -2, -3, -4)
출력결과
-1
```

##### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

정해지지 않은 키워드 인자들은 **`dict`** 형태로 처리가 되며, `**`로 표현합니다. 

보통 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

---

**활용법**

```python
def func(**kwargs):
```
> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미

------------------

# Python 05 workshop, homework

```python
my = {
    "혜인" : "3",
    "우중" : "4"
}
print(my.keys())

for i in my.keys():
    print(i)
---------------------------------------------------------------
출력결과
dict_keys(['혜인', '우중'])
혜인
우중-
```

