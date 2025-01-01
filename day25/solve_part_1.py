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

    i = 0
    grids = []
    grid = []

    while i < len(lines):
        if lines[i] == '':
            grids.append(grid)
            grid = []
            i += 1
            continue
        grid.append(lines[i])
        i += 1
    grids.append(grid)

    keys = []
    locks = []

    for grid in grids:
        if all([x == '#' for x in grid[0]]):
            locks.append(grid)
        else:
            keys.append(grid)

    def overlap(key, lock):
        M = len(lock)
        N = len(lock[0])

        occupied = set([(r, c) for r in range(M)
                       for c in range(N) if lock[r][c] == '#'])
        inValid = False
        for r in range(M):
            for c in range(N):
                if key[r][c] == '#' and (r, c) in occupied:
                    inValid = True
                    break
            if inValid:
                break
        return inValid

    res = 0
    for key in keys:
        for lock in locks:
            if not overlap(key, lock):
                res += 1
    pr(res)


if __name__ == '__main__':
    main()
