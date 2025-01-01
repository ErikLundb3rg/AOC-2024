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


def main():
    lines = getLines('input.in')

    towels = list(set(lines[0].split(', ')))

    targets = lines[2:]

    memo = {}

    def possible(remaining):
        if remaining in memo:
            return memo[remaining]
        if remaining == '':
            return True

        res = False
        for towel in towels:
            if remaining.startswith(towel):
                if possible(remaining[len(towel):]):
                    res = True
        memo[remaining] = res
        return res

    cnt = 0
    for i, target in enumerate(targets):
        if possible(target):
            cnt += 1
    pr(cnt)


if __name__ == '__main__':
    main()
