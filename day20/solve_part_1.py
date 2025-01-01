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

    grid = [list(row) for row in lines]
    M = len(grid)
    N = len(grid[0])
    source, target = None, None

    for r in range(M):
        for c in range(N):
            if grid[r][c] == 'S':
                source = (r, c)
            elif grid[r][c] == 'E':
                target = (r, c)
    # do dijkstra from source but with (distance, position, jumps)
    # go over pairs of positions
    # if their absolute is less or equal to 2 and not
    # used before as cheat pair,
    # try dijkstra from a to source and b to target
    # check if summed distance + 2 is better than best

    def neighbor(a, b):
        r, c = a
        rr, cc = b
        for dR, dC in DIRECTIONS:
            if (rr+dR, cc+dC) == (r, c):
                return True
        return False

    def dijkstra(jumps, start, end, targetDistance=None):
        from heapq import heappush, heappop
        q = [(0, start, (-1, -1), (-1, -1), jumps)]
        visited = set()  # (r, c, j1, j2)
        solves = []

        while q:
            distance, (r, c), j1, j2, jumps = heappop(q)

            if targetDistance and distance >= targetDistance:
                continue

            if (r, c) == end:
                solves.append((distance, j1, j2))
                continue
            if not (0 <= r < M and 0 <= c < N):
                continue
            if grid[r][c] == '#' and jumps == 0:
                continue
            if (r, c, j1, j2) in visited:
                continue
            if grid[r][c] == '#':
                if j1 == (-1, -1):
                    j1 = (r, c)
                else:
                    if not neighbor(j1, (r, c)):
                        continue
                    j2 = (r, c)
                jumps -= 1
                assert jumps >= 0
            visited.add((r, c, j1, j2))

            for dR, dC in DIRECTIONS:
                nR, nC = r+dR, c+dC
                heappush(q, (distance+1, (nR, nC), j1, j2, jumps))
        return solves

    ref = dijkstra(0, source, target)[0]
    SAVING_TARGET = 100
    others = dijkstra(1, source, target, ref[0]-SAVING_TARGET)
    from collections import defaultdict
    mp = defaultdict(int)

    def pg():
        for row in grid:
            print("".join(row))
        print()

    for value in others:
        diff = ref[0]-value[0]
        j1, j2 = value[1], value[2]
        mp[diff] += 1
    print(sum(mp.values()))


if __name__ == '__main__':
    main()
