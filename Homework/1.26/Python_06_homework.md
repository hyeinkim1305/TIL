# Python_06_homework



### 1. 

```
number = [3,4,9,6] 일 때
number.sort()
하게 되면 
number = [3,4,6,9]가 되고,

number = [3,4,9,6] 일 때
sorted(number)하게 되면 이 자체로 
[3,4,6,9]가 된다.
즉, sort()는 원본을 변형하고 none을 리턴하며, sorted는 sorted된 것을 반환한다.
```



### 2.

```
abc = ['a','b','c']일 때, 
abc.append('dd') 하면 abc = ['a','b','c','dd'] 이렇게 되는데

abc = ['a','b','c']일 때, 
abc.exted(['dd']) 해야 abc = ['a','b','c','dd'] 이렇게 된다. 
abc.extend('dd')하게 되면 abc = ['a','b','c','dd','d','d'] 이렇게 된다.
```





### 3.

```
같다. 왜냐하면 shallow 복사 되었기때문에 둘 다 같은 주소를 가리키고 있어서 값이 같아진다. 
```

