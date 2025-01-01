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
    start = (0, 0)
    target = (70, 70)
    LIMIT = 1024

    blocked = set()
    for line in lines[:LIMIT]:
        r, c = map(int, line.split(','))
        blocked.add((r, c))

    from heapq import heappop, heappush

    q = [(0, start)]

    res = None

    while q:
        dist, (r, c) = heappop(q)

        if (r, c) == target:
            res = dist
            break

        if not (0 <= r <= target[0] and 0 <= c <= target[1]):
            continue

        if (r, c) in blocked:
            continue

        blocked.add((r, c))

        for dR, dC in DIRECTIONS:
            nR, nC = r+dR, c+dC
            heappush(q, (dist+1, (nR, nC)))
    pr(res)


if __name__ == '__main__':
    main()
