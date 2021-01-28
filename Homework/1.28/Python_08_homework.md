# Python_08_homework

### 1.

```python
circle = Circle(3,2,4)
circle.area()
circle.circumference()
```



### 2.

```python
class Dog(Animal):
    
    def __inint__(self, name):
        super().__init__(name)
        
    def bark(self):
        print(f'{self.name}! 짖는다!')
        
    def walk(self):
        print(f'{self.name}! 달린다!')

        
class Bird(Animal):
    
    def __inint__(self, name):
        super().__init__(name)
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
        
    def fly(self):
        print(f'{self.name}! 푸더덕!')
        
```



### 3.

```
ZeroDivisionError : 0으로 나눌 때 나온다.
NameError : 정의되지 않은 변수를 호출하였을 때 나오나.
TypeError : 타입이 잘못 되었거나 함수 호출과정에서 문제가 있을 때 나온다.
IndexError : 존재하지 않는 index로 조회하였을 때 나온다.
KeyError : 딕셔너리에 키가 없을 때 나온다.
ModuleNotFoundError : 모듈을 찾을 수 없을 때 나온다.
ImportError : 모듈은 있으나 가져올 때 실패하면 생긴다. 존재하지 않는 클래스나 함수 호출이 그 예시이다. 

```

