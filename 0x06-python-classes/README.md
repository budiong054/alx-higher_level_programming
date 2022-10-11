### 0X06. Python - Classes and Objects

[0-square.py]() contains an empty class `Square` that defines a square

[1-square.py]() contains a class `Square` that defines a square by: (based on [0-square.py]())
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)

[2-square.py]() contains a class `Square` that defines a square by: (based on [1-square.py]())
* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
	- size must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
	- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
