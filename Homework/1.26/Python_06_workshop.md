# Python_06_workshop

### 1.

```python
def duplicated_letters(word):
    s = []
    words = set(word)
    for w in words:
        if word.count(w) > 1:
            s.append(w)
    return s
```





### 2.

```python
def low_and_up(word):
    
    ww = []
    for i,w in enumerate(word):
        if i % 2 == 0:
            ww.append(w.lower())
        else:
            ww.append(w.upper())
            
    return ''.join(ww)
```



### 3.

```python
def lonely(numbers):
    
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1]:
            numbers[i] = 1000
        else:
            continue
    for i in range(numbers.count(1000)):
        numbers.remove(1000)
            
    return numbers
```

