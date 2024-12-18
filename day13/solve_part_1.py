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


def main():
    lines = getLines('input.in')

    res = 0
    for i in range(0, len(lines), 4):
        A = parseXY(lines[i])
        B = parseXY(lines[i+1])
        tX, tY = parseXY(lines[i+2])
        minCost = [None]
        cCost = 3
        dCost = 1
        visited = set()

        def solve(C, D, nrC, nrD, x, y, tX, tY, cost):
            if minCost[0] != None or (nrC, nrD) in visited or x > tX or y > tY:
                return
            if (x, y) == (tX, tY):
                minCost[0] = cost
                return

            visited.add((nrC, nrD))
            dCX, dCY = C
            dDX, dDY = D
            solve(C, D, nrC+1, nrD, x+dCX, y+dCY, tX, tY,  cost + cCost)
            solve(C, D, nrC, nrD+1, x+dDX, y+dDY, tX, tY, cost + dCost)

        C, D = getAB(A, B)
        if D == A:
            cCost, dCost = dCost, cCost
        solve(C, D, 0, 0, 0, 0, tX, tY, 0)
        if minCost[0] is not None:
            res += minCost[0]
    pr(res)


if __name__ == '__main__':
    main()
