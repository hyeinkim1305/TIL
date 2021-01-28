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
```

