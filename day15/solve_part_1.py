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
    robot = (-1, -1)
    grid = []
    takingGrid = True
    movements = []

    for line in lines:
        if not line.strip():
            takingGrid = False
            continue
        if takingGrid:
            grid.append(list(line))
        else:
            movements.extend(line)

    M = len(grid)
    N = len(grid[0])

    for r in range(M):
        for c in range(N):
            if grid[r][c] == '@':
                robot = (r, c)

    signToMovement = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    r, c = robot
    for m in movements:
        grid[r][c] = '.'
        dR, dC = signToMovement[m]

        nR, nC = r+dR, c+dC

        if grid[nR][nC] == '.':
            r, c = nR, nC
        elif grid[nR][nC] == 'O':
            bR, bC = nR, nC
            while grid[bR][bC] == 'O':
                bR += dR
                bC += dC
            if grid[bR][bC] == '.':
                grid[bR][bC] = 'O'
                grid[nR][nC] = '.'
                r, c = nR, nC
        grid[r][c] = '@'

    res = 0
    for r in range(M):
        for c in range(N):
            if grid[r][c] == 'O':
                res += (r*100)+c

    for row in grid:
        print("".join(row))
    pr(res)


if __name__ == '__main__':
    main()
