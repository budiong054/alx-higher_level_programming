#!/usr/bin/python3
for num in range(0, 26):
    if num % 2 == 0:
        num = 122 - num
    else:
        num = 90 - num
    print("{:c}".format(num), end="")
