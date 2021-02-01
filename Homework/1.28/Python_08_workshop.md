# Python_08_workshop

```python
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
class Rectangle(Point):
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y) 
    
    def get_perimeter(self):
        return ((self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)) * 2
    
    def is_square(self):
        
        if (self.p2.x - self.p1.x) == (self.p1.y - self.p2.y):
            return True
        else:
            return False
        
# 교수님 풀이
class Rectangle(Point):
    
    def __init__(self, a, b):  # 여기 a, b잘보기 나는 안했음 이거를 !
        self.p1 = a
        self.p2 = b
        self.width = (self.p2.x - self.p1.x)   # 이런 식으로 해도 된다!
        self.height = (self.p1.y - self.p2.y) 
        
        
    .....
```

