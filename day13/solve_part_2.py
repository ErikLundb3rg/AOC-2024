import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc
import numpy as np
sys.setrecursionlimit(int(1e6))


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def neighbors(r, c):
    return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]


def pr(s):
    print(s)
    pc.copy(s)


def parseXY(line):
    right = line.split(': ')[1]
    p = right.split(', ')
    x, y = p[0][2:], p[1][2:]
    return int(x), int(y)


def getAB(A, B):
    x, y = A[0] / 3, A[1] / 3
    c, d = B

    if min(x, y) < min(c, d):
        return B, A
    return A, B


# I DID NOT WRITE THIS, courtesy of reddit: xelf
def solve(ax, ay, bx, by, px, py):
    M = np.array([[ax, bx], [ay, by]])
    P = np.array([px, py]) + 10000000000000
    a, b = map(round, np.linalg.solve(M, P))
    return a*3+b if [a*ax+b*bx, a*ay+b*by] == [*P] else 0


def main():
    lines = getLines('input.in')

    res = 0
    for i in range(0, len(lines), 4):
        A = parseXY(lines[i])
        B = parseXY(lines[i+1])
        tX, tY = parseXY(lines[i+2])
        ax, ay = A
        bx, by = B
        res += solve(ax, ay, bx, by, tX, tY)
    pr(res)


if __name__ == '__main__':
    main()
