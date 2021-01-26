# Python_05_homework

### 1.

```python
def count_vowels(word):
    num = 0
    num = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')

    return num

-----------------------------------------------------------

def count_vowels(word):
    vowels = 'aeiou'
    result = 0
    for vowel in vowels:
        if vowel in word:
            result += word.count(vowel)
    return result
# 즉 거꾸로 푸는 것이 좋다!
```



### 2. 

```
(4)
```



### 3. 

```python
def only_square_area(n,m):
    square = []
    for i in n:
        if i in m:
            square.append(i*i)
        else:                           # else, continue 안해도 된다.
            continue
    return square
```

