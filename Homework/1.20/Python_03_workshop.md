# Python_03_workshop

#### 

list로 하는거 잘 보기



### 1.

```
def list_sum(n):
    result = 0
    for i in range(len(n)):
        result += n[i]
    return result
    
# sol2
def list_sum(int_list):
    total = 0
    for i in int_list:
        total += i
    return total
```



### 2.

```
def dict_list_sum(n):
    result = 0
    for i in range(len(n)):
        result += n[i]['age']
    return result
    
# sol2
def dict_list_sum(n):
    for i in n:
        result += i['age']
    return result
    
# sol3
def dict_list_sum(num):
    result = 0
    for i in num:
        result += i.get('age')
    return result

```



### 3. 

```
def all_list_sum (n):
    result = 0
    for i in range(len(n)):
        for j in range(len(n[i])):
            result += n[i][j]
    return result
    
# sol2
def all_list_sum(my_list):
    total = 0
    for mymy_list in my_list:
        for num in mymy_list:
            total += num
    return total
    
# sol3
def all_list_sum(num):
    result = 0
    for i in num:
        for j in i:
            result += j
    return result
```

