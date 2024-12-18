import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def neighbors(r, c):
    return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]


def pr(s):
    print(s)
    pc.copy(s)


def main():
    lines = getLines('input.in')


if __name__ == '__main__':
    main()
