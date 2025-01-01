import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def pr(s):
    print(s)
    pc.copy(s)


def main():
    lines = getLines('input.in')

    grid = [list(row) for row in lines]
    M = len(grid)
    N = len(grid[0])
    source = None
    target = None

    def printGrid():
        for row in grid:
            print("".join(row))

    for r in range(M):
        for c in range(N):
            if grid[r][c] == 'S':
                source = (r, c)
            if grid[r][c] == 'E':
                target = (r, c)

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # dijstra with: (points, r, c, direction)
    # neighbors are other r, c which are not visited and ofc might have new direction
    from heapq import heappop, heappush

    sR, sC = source
    q = [(0, sR, sC, (0, 1))]
    visited = set()
    res = None

    while q:
        points, r, c, d = heappop(q)

        if (r, c) == target:
            res = points
            break
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))

        nR, nC = r+d[0], c+d[1]

        if grid[nR][nC] != '#':
            heappush(q, (points+1, r+d[0], c+d[1], d))

        dB = DIRECTIONS[DIRECTIONS.index(d)-1]
        dA = DIRECTIONS[(DIRECTIONS.index(d)+1) % len(DIRECTIONS)]

        for nD in [dB, dA]:
            rr, cc = r+nD[0], c+nD[1]
            if grid[rr][cc] != '#':
                heappush(q, (points+1001, rr, cc, nD))

    pr(res)


if __name__ == '__main__':
    main()
