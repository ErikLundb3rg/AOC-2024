import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc


def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# using inspiration from https://github.com/jonathanpaulson
# getting this to run in a reasonable time was hard


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
    from collections import deque

    DIST = {}
    Q = deque([(0, target[0], target[1])])
    while Q:
        d, r, c = Q.popleft()
        if (r, c) in DIST:
            continue
        DIST[(r, c)] = d
        for dr, dc in DIRECTIONS:
            rr, cc = r+dr, c+dc
            if 0 <= rr < M and 0 <= cc < N and grid[rr][cc] != '#':
                Q.append((d+1, rr, cc))

    def dijkstra(start, end, maxTime, minSave, targetDistance=None):
        q = deque([(0, start, None, None, None)])
        visited = set()  # (r, c, j1, j2)
        solves = set()

        while q:
            distance, (r, c), startCheat, endCheat, time = q.popleft()
            assert endCheat is None

            if distance >= targetDistance-minSave:
                continue

            if grid[r][c] == 'E':
                if endCheat == None:
                    endCheat = (r, c)
                if distance <= targetDistance and (startCheat, endCheat) not in solves:
                    solves.add((startCheat, endCheat))

            key = (r, c, startCheat, endCheat, time)
            if key in visited:
                continue
            visited.add(key)
            if startCheat == None:
                q.append((distance, (r, c), (r, c), None, maxTime))
            if time is not None and grid[r][c] != '#':
                if DIST[(r, c)] <= targetDistance - minSave - distance:
                    solves.add((startCheat, (r, c)))
            if time == 0:
                continue
            else:
                for dR, dC in DIRECTIONS:
                    nR, nC = r+dR, c+dC
                    if time != None:
                        assert time > 0
                        if 0 <= nR < M and 0 <= nC < N:
                            q.append(
                                (distance+1, (nR, nC), startCheat, None, time-1))
                    else:
                        if 0 <= nR < M and 0 <= nC < N and grid[nR][nC] != '#':
                            q.append(
                                (distance+1, (nR, nC), startCheat, endCheat, time))
        return len(solves)
    res = dijkstra(source, target, 20, 100, DIST[source])
    pr(res)


if __name__ == '__main__':
    main()
