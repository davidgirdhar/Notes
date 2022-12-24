### Typeerror: str object is not callable – How to Fix in Python

This error generally arise due to naming of variables or functions same as prefined keywords of a programming language.
For example ,here we discuss one of those cases 

`TypeError: 'str' object is not callable`
Now this error mainly occur when :
 * You pass a variable named type or any other variable(name same as keywords) as a parameter to the str() function.Now type is a keyword in python language.
    ```python
    type = "hello"
    print(type(str(type)))
    ```
    `TypeError: 'str' object is not callable`
    The result was the TypeError: 'str' object is not callable error. This is happening because we are using a variable name that the compiler already recognizes as something different.
    This can be fixed by changing variable name.

 * When you call a string like a function.



### ValueError: index 0 is out of bounds for axis 0 with size 0

In numpy, index and dimension numbering starts with 0. So axis 0 means the 1st dimension. Also in numpy a dimension can have length (size) 0. The simplest case is:
 import numpy as np
``` python 
arr = np.zeros((0,), int)
print(arr)
```
`array([], dtype=int32)`

``` python 
arr[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index 0 is out of bounds for axis 0 with size 0
```

