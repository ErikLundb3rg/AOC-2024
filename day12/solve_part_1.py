import sys
import re
from collections import defaultdict, Counter, deque
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
    grid = lines

    visited = set()
    M = len(lines)
    N = len(lines[0])
    price = 0

    for bR in range(M):
        for bC in range(N):
            if (bR, bC) not in visited:
                q = [(bR, bC)]
                region = grid[bR][bC]
                area = 0
                perimeter = 0
                visited.add((bR, bC))

                while q:
                    r, c = q.pop(0)

                    area += 1

                    for nR, nC in neighbors(r, c):
                        if not (0 <= nR < M and 0 <= nC < N):
                            perimeter += 1
                            continue
                        if grid[nR][nC] != region:
                            perimeter += 1
                            continue
                        if (nR, nC) in visited:
                            continue
                        visited.add((nR, nC))
                        q.append((nR, nC))
                price += area*perimeter
    pr(price)


if __name__ == '__main__':
    main()
