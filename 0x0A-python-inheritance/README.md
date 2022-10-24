# 0x0A. Python - Inheritance

### 0. Lookup
[0-lookup.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py) contains a function that returns the list of available attributes and methods of an object
- Prototype: `def lookup(obj):`

### 1. My list
[1-my\_list.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py) contains a class `MyList` that inherits from `list`
- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
[tests/1-my\_list.txt](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/tests/1-my_list.txt) contains the doctest for the class `MyList`

### 2. Exact same object
[2-is\_same\_class.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/2-is_same_class.py) contains a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.
- Prototype: `def is_same_class(obj, a_class):`

### 3. Same class or inherit from
[3-is\_kind\_of\_class.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/3-is_kind_of_class.py) contains a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.
- Prototype: `def is_kind_of_class(obj, a_class):`

### 4. Only sub class of
[4-inherits\_from.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/4-inherits_from.py) contains a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.
- Prototype: `def inherits_form(obj, a_class):`

### 5. Geometry module
[5-base\_geometry.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/5-base_geometry.py) contains an empty class `BaseGeometry`.

### 6. Improve Geometry
[6-base\_geometry.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py) contains a class `BaseGeometry` (based on [5-base\_geometry.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/5-base_geometry.py) ).
- Public instance method: `def area(self):` that raises an `Exception` with the message `area()` is not implemented

### 7. Integer validator
[7-base\_geometry.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py) contains a class `BaseGeometry` (based on [6-base\_geometry.py](https://github.com/budiong054/alx-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py) ).
- Public instance method: `def integer_validator(self, name, value):` that validates `value`
