# Python_08_homework

### 1.

```python
circle = Circle(3,2,4)
circle.area()
circle.circumference()

# self.pi는 Circle.pi 이런식으로 해야한다. 클래스변수이니까 // 음 self.x 이런거는 변수가 되는 듯한 느낌이넹! 
```



### 2.

```python
class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name)  #여기서는 이거를 안써도 되기는 함. 그런데 만약 부모클래스에 있는 name외에 다른 것을 더 넣으려고 한다면 이거는 부모에 있는거를 긁어오는 느낌이니까 쓰는 것이 좋다 (convention)
        
    def bark(self):
        print(f'{self.name}! 짖는다!')
        
    def walk(self):    # 오버라이딩
        print(f'{self.name}! 달린다!')

        
class Bird(Animal):
    
    def __init__(self, name):
        super().__init__(name)
        
    def eat(self):     # 이거는 재정의할 필요가 없다!!
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

