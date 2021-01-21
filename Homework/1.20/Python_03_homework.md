# Python_03_homework

##### 

### 1.

```
set()
sorted()
sum()
str()
range()
list()
또는
print(dir(__builtins__))
```



### 2.

```
def get_middle_char(s):
    
    if len(s) % 2 == 1:
        num = len(s) // 2
        return s[num]
    else:
        num = len(s) // 2
        return s[num-1:num+1]
```

여기 num-1, num+1 부분 잘 보기! 헷갈리지 말기

문자열도 인덱싱 접근이 가능한거 명심 !

### 3. 

```
(4)
```



### 4. 

```
None
```



### 5. 

```
def my_avg(*args):
    result = 0
    for num in args:
        result += num
        
        avg = result / len(args) 

    return avg
```

```
# sol2
def my_avg(*arg):
    sum_arg = 0
    count = 0
    for i in arg:
        sum_arg += i
        count += 1
    return sum_arg / count
print(my_avg(77, 83, 95, 80, 70))
```

