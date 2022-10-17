### 0x08. Python - More Classes and Objects

[0-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/0-rectangle.py) contains an empty class `Rectangle` that defines a rectangle

[1-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/1-rectangle.py) contains a class `Rectangle` that defines a rectangle by: (based on [0-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/0-rectangle.py)
- Private instance attribute: `width`
- Private instance attribute: `height`
- Instantiation with optional `width` `height`: `def __init__(self, width=0, height=0):`

[2-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/2-rectangle.py) contains a class `Rectangle` that defines a rectangle by: (based on [1-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/1-rectangle.py)
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self);` that returns the rectangle perimeter

[3-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/3-rectangle.py) contains a class `Rectangle` that defines a rectangle by: (based on [2-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/2-rectangle.py)
- `print()` and `str()` should print the rectangle with the character `#`

[4-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/4-rectangle.py) contains a class `Rectangle` that defines a rectangle by: (based on [3-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/3-rectangle.py)
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

[5-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/5-rectangle.py) contains a class `Rectangle` that defines a rectangle by: (based on [4-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/4-rectangle.py)
- Print the message `Bye rectangle...` (`...` begin 3 dots not ellipsis) when an instance of `Rectangle` is deleted

[6-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/6-rectangle.py) contains a class `Rectangle` that defines a rectangle by: (based on [5-rectangle.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x08-python-more_classes/5-rectangle.py)
- Public class attribute `number_of_instances`:
	- Initialized to 0
	- Incremented during each new instance instantiation
	- Decremented during each instance deletion
