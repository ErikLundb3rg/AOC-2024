import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def pr(s):
    print(s)
    pc.copy(s)


MOD = 16777216


def evolve(num):
    s1 = ((num*64) ^ num) % MOD
    s2 = ((s1 // 32) ^ s1) % MOD
    s3 = ((s2*2048) ^ s2) % MOD
    return s3


def main():
    lines = getLines('input.in')

    nums = [int(x) for x in lines]

    sm = 0
    for num in nums:
        res = num
        for _ in range(2000):
            res = evolve(res)
        sm += res
    print(sm)


if __name__ == '__main__':
    main()
