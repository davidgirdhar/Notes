##### MRO(Method Resolution Order) 

```python
class Class1:
    def m(self):
        print("In Class1")

class Class2():
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class1):
    def m(self):
        # Using super() to call the next method in MRO order
        super().m()
        print("In Class4")

obj = Class4()
obj.m()
```

    Now here Class4 inherits Class2 m() method not Class1 because of MRO, so Class4's MRO is determined based on the order of inheritance (left-to-right) and depth.Since Class2 appears before Class1