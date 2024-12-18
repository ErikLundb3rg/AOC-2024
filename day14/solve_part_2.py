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
    TIMES = 10000000

    for seconds in range(TIMES):
        for i in range(len(points)):
            x, y = points[i]
            dX, dY = velocities[i]
            nX = (x + (dX)) % WIDTH
            nY = (y + (dY)) % HEIGHT
            points[i] = (nX, nY)

        if len(set(points)) == len(points):
            print(seconds)
            matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

            for x, y in points:
                matrix[y][x] += 1

            for row in matrix:
                xs = [str(x) for x in row]
                f = [x if x != '0' else '.' for x in xs]
                print("".join(f))
            break


if __name__ == '__main__':
    main()
