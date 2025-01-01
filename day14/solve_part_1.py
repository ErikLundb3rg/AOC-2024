import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc
from operator import mul


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
    points = []
    velocities = []

    for line in lines:
        a, b = line.split(' ')
        x, y = map(int, a[2:].split(','))
        dX, dY = map(int, b[2:].split(','))
        points.append((x, y))
        velocities.append((dX, dY))

    WIDTH = 101
    HEIGHT = 103
    TIMES = 100
    res = []
    for (x, y), (dX, dY) in zip(points, velocities):
        nX = (x + (TIMES*dX)) % WIDTH
        nY = (y + (TIMES*dY)) % HEIGHT
        res.append((nX, nY))

    quadrants = [0 for _ in range(4)]
    for x, y in res:
        if x == WIDTH // 2 or y == HEIGHT // 2:
            continue
        if x < (WIDTH // 2):
            if y < (HEIGHT // 2):
                quadrants[0] += 1
            else:
                quadrants[1] += 1
        else:
            if y < (HEIGHT // 2):
                quadrants[2] += 1
            else:
                quadrants[3] += 1
    print(quadrants)
    p = 1
    for z in quadrants:
        p *= z
    print(p)


if __name__ == '__main__':
    main()
