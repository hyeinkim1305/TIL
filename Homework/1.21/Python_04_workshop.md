# Python_04_workshop

### 1.

```
def get_secret_word(s):
    ss = ''
    for i in s:
        ss+=(chr(i))
    return ss
```



### 2. 

```
def get_secret_number(s):
    result = 0
    for i in s:
        result += ord(i)
    return result
```



### 3.

```
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
        
```

