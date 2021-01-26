# Python_05_workshop

### 1.

```python
def get_dict_avg(n):
    ans = 0
    count = 0
    for i in n.keys():     # 그냥 n 이라고 해도 key값들에 접근 가능!
        ans += n.get(i)
        count += 1
    avg = ans / count
    
    return avg

-------------------------------------------------------------------------

def get_dict_avg(students):
    scores = []
    for student in students:
        scores.append(students[student])
    result = sum(scores) / len(scores)
    return result

-------------------------------------------------------------------------

def get_dict_avg(students):
    scores = []
    for student in students.values:
        scores.append(student)
    result = sum(scores) / len(scores)
    return result
```



### 2. 

```python
def count_blood(n):
    my_dict = {}
    my_dict['A'] = n.count('A')
    my_dict['B'] = n.count('B')
    my_dict['O'] = n.count('O')
    my_dict['AB'] = n.count('AB')

    return my_dict

-----------------------------------------------------------------------

def count_blood(blood_types):
    blood_type = {}
    for blood in blood_types:
        if blood not in blood_type:
            blood_type[blood] = 1
        else:
            blood_type[blood] += 1
    return blood_type

---------------------------------------------------------------------------

def count_blood(blood_types):
    blood_type = {}
    for blood in blood_types:
        blood_type[blood] = blood_types.count(blood)
    return blood_type

---------------------------------------------------------------------

def count_blood(blood_types):
    blood_type = {}
    for blood in blood_types:
        # 있으면 가져온 다음에 1을 더하고 없으면 0으로 하고 1을 더하고 
        blood_type[blood] = blood_type.get(blood,0) + 1
    return blood_type
```

