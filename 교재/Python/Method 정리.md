# Method 정리 / 한번씩 영향미치는건 뭐지?

# (순서 : Str -> List -> Set -> Dict)

string, tuple, range는 immutable 변경불가능한 변수

## String

> 변경할 수 없고(immutable), 순서가 있고(ordered), 순회가능한(iterable)

#### String의 다양한 조작법(method)

- .find(x)

  - x의 **첫 번째 위치**를 반환합니다. 없으면, `-1`을 반환합니다.

- .index(x)

  - x의 **첫 번째 위치**를 반환합니다. 없으면, 오류가 발생합니다.

- .replace(old, new[, count])

  - old를 new로 바꿔서 반환합니다.

  - count를 지정하면 해당 갯수 만큼만 시행합니다.

    `z = 'zoo!yoyo!' z.replace('o','') => 'z!yy!' z.replace('o','',2) =. 'z!yoyo!'`
    
  - **count를 지정하지 않으면 다 바꿔버린다!! 주의**

- .strip([chars])

  - 특정한 문자를 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다.(rstrip). 지정하지 않으면 공백을 제거합니다.
  - **특정 문자를 지정하면 하나씩 지워지는게 아니라 양쪽 끝에서부터 지워진다!**

- .split()

  - 문자열을 특정한 단위로 나누어 리스트로 반환합니다.
  - **() 괄호 안에 들어가있는 단위로 나누는** 것

- 'separator'.join(iterable)

  - 특정한 문자열로 만들어 반환합니다.

  - 반복가능한(literable) 컨테이너의 요소들을 separator를 구분자로 합쳐(`join()`) 문자열로 반환합니다.

    `word = '배고파' words = ['안녕', 'hello'] '!'.join(word) => '배!고!파' ','.join(words) => '안녕,hello'`

  - **() 괄호 안에 있는 거를 ' '안에 들어있는거를 사이에 넣는 것**

  - **주의할 사항 : join은 문자열 형태일 때 붙일 수 있다! 리스트, set 붙일 수 있는데 문자열일 경우만 가능 ( str 이나 map 활용해서 안에 요소들 문자형태로 바꾸기! )**

- .capitalize(), .title(), `.upper()`, `.lower()`, `.swapcase()`

- **enumerate 문자열에서도 사용이 가능하다.**

## LIst

> 변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

#### List의 다양한 조작법(method)

- .append(x)

  - 리스트에 값을 추가할 수 있습니다.

- .extend(iterable)

  - 리스트에 literalbe(list, range, tuple, string**[주의]**) 값을 붙일 수가 있습니다.

    `cafe = ['starbucks', 'tomntoms', 'hollys'] cafe.extend(['ediya']) => ['starbucks', 'tomntoms', 'hollys', 'ediya'] cafe.extend('home') => ['starbucks', 'tomntoms', 'hollys', 'ediya', 'h', 'o', 'm', 'e']`

- .insert(i, x)

  - 정해진 위치 `i`에 값을 추가합니다.

- .remove(x)

  - 리스트에서 값이 x인 것을 삭제합니다.
  - **하나씩 삭제된다.**

- .pop(i)

  - 정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환합니다.

  - `i`가 지정되지 않으면 마지막 항목을 삭제하며, 그 항목을 반환합니다.

    `a = [1, 2, 3, 4, 5] print(f'{a.pop()} 삭제 {a}') => '5 삭제 [1, 2, 3, 4]'`

- .clear()

  - 리스트의 모든 항목을 삭제합니다.

- .index(x)

  - x 값을 찾아 해당 index 값을 반환합니다.

- .count(x)

  - 원하는 값의 갯수를 확인할 수 있습니다.

- .sort()

  - 정렬을 합니다.

  - 내장함수 `sorted()`와는 다르게 **원본 list를 변형**시키고, `None`을 리턴합니다.

    `a = [2, 1, 5, 4, 3] a.sort() print(a) => [1, 2, 3, 4, 5] print(sorted(a)) => [1, 2, 3, 4, 5]`

- .reverse()

  - 반대로 뒤집습니다.(정렬 아님)

    `students = ['최예원', '배유빈', '김지호'] students.reverse() print(students) => ['김지호', '배유빈', '최예원']`

- 복사방법 3가지

  - [:] 슬라이싱
  - list()
  - 2차원 배열 복사 : b = copy.deepcopy(a)

## Set

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable), **중복이 없다**

#### Set의 다양한 조작법(method)

- .add(elem)

  - elem을 세트에 추가합니다.
  - **순서가 상관이 없다.**

- .update(*others)

  - 여러가지의 값을 추가합니다.

  - 인자로는 반드시 iterable 데이터 구조를 전달해야합니다.

    `a = {'사과', '바나나', '수박'} a.update(('파인애플', '애플')) print(a) => {'수박', '애플', '바나나', '사과', '파인애플'}`

- .remove(elem)

  - elem을 세트에서 삭제하고, 없으면 KeyError가 발생합니다.

- .discard(elem)

  - elem을 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.

- .pop()

  - **임의의 원소**를 제거해 반환합니다.

## Dictionary

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)

#### Dictionary의 다양한 조작법(method)

- .get(key[, default])

  - key를 통해 value를 가져옵니다.

  - 절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.

    `my_dict = ['apple': '사과', 'banana': '바나나',] my_dict.get('pineapple', 0) => None을 return my_dict.get('pineapple', 0) => 0을 return`

  - my_dict.get('pineapple',0) : 해당하는 키값이 없으면 0을 리턴한다.

- .pop(key[, default])

  - key가 dictionary에 있으면 제거하고 그 값을 반환합니다. 그렇지 않으면 default를 반환합니다.
  - defauly가 없는 상태에서 dictionary에 없으면 KeyError가 발생합니다.
  - 키값에 해당하는 키와 value를 삭제한다. 

- .update()

  - 값을 제공하는 key, value로 덮어씁니다.

    `my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'} my_dict.update({'banana': '빠나나'}) print(my_dict) = {'apple': '사과', 'banana': '빠나나', 'melon': '멜론'}`

- 반복문 순회

  - for문을 딕셔너리안에서 순회하면 보통은 key를 순회하는 것!

    dict.keys()

    dict.values()

    dict.items()



## map(function, iterable)

* 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려준다. 


* return은 `map_object` 형태이다.



## filter(function, iterable)

* **iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환한다.**


* `filter object` 를 반환한다.



## zip(*iterables)

* 복수의 iterable 객체를 모아(`zip()`)준다.


* 결과는 튜플의 모음으로 구성된 `zip object` 를 반환한다.



## 기타 다른 함수들, 표현들

- max, min
- sum
- sorted(a), sorted(a, reverse = True)
- enumerate
- [::-1], [0::2]       ->      0부터 끝까지 2씩 건너뛰어서
- .count('a')      ->      a 개수
- key = lambda x : x[0]     ->  x[0] 을 기준으로 정렬