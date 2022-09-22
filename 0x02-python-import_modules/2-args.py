#!/usr/bin/python3
import sys

if __name__ == '__main__':
    length = len(sys.argv)
    if length < 2:
        print(f"{length - 1:d} arguments.")
    else:
        if length == 2:
            print(f"{length - 1:d} argument:")
        else:
            print(f"{length - 1:d} arguments:")
        for i in range(1, length):
            print(f"{i:d}: {sys.argv[i]}")
