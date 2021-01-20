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



### 3. 

```
(4)
```



### 4. 

```
none
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

