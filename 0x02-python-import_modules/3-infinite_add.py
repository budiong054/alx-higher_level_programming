#!/usr/bin/python3
import sys

if __name__ == '__main__':
    num_len = len(sys.argv)
    add = 0
    for num in range(1, num_len):
        add += int(sys.argv[num])
    print("{:d}".format(add))
