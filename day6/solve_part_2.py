import math
from itertools import combinations


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def isSquare(points):
    from collections import defaultdict
    mp = defaultdict(int)
    for a, b in points:
        mp[a] += 1
        mp[b] += 1

    for key in mp.keys():
        if mp[key] < 2:
            return False
    return True


def main():
    lines = getLines('input.in')

    grid = [list(row) for row in lines]
    lines = grid

    M = len(lines)
    N = len(lines[0])
    pos = None

    for r in range(M):
        for c in range(N):
            if lines[r][c] == '^':
                pos = (r, c)
                break

    res = 0

    for bR in range(M):
        for bC in range(N):
            print(bR, bC)
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            r, c = pos
            dR, dC = dirs[0]
            visited = set()
            while True:
                if (r, c, dR, dC) in visited:
                    res += 1
                    break
                visited.add((r, c, dR, dC))
                nR, nC = r+dR, c+dC
                if not (0 <= nR < M and 0 <= nC < N):
                    break
                if lines[nR][nC] == '#' or (nR, nC) == (bR, bC):
                    newIdx = (dirs.index((dR, dC)) + 1) % len(dirs)
                    dR, dC = dirs[newIdx]
                else:
                    r, c = nR, nC
    print(res)


if __name__ == '__main__':
    main()
