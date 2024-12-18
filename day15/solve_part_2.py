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

    def printGrid():
        for row in grid:
            print("".join(row))

    for line in lines:
        if not line.strip():
            takingGrid = False
            continue
        if takingGrid:
            row = []
            for value in line:
                if value == '#':
                    row.extend(list('##'))
                elif value == 'O':
                    row.extend(list('[]'))
                elif value == '.':
                    row.extend(list('..'))
                elif value == '@':
                    row.extend(list('@.'))
            grid.append(row)
        else:
            movements.extend(line)

    # printGrid()
    M = len(grid)
    N = len(grid[0])

    for r in range(M):
        for c in range(N):
            if grid[r][c] == '@':
                robot = (r, c)

    def getBox(r, c):
        if grid[r][c] == '[':
            return [(r, c), (r, c+1)]
        if grid[r][c] == ']':
            return [(r, c), (r, c-1)]

    signToMovement = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    def combinedBox(r, c, dR, dC, checked):
        if grid[r][c] not in '[]':
            return []
        if (r, c) in checked:
            return []

        boxCoords = getBox(r, c)
        other = []
        for rr, cc in boxCoords:
            checked.add((rr, cc))
            other += combinedBox(rr+dR, cc+dC, dR, dC, checked)
        return boxCoords + other

    def possible(r, c, dR, dC, checked):
        if grid[r][c] == '#':
            return False
        if grid[r][c] == '.':
            return True
        if (r, c) in checked:
            return True

        checked.add((r, c))
        boxCoords = getBox(r, c)
        # print(r, c, dR, dC)
        for rr, cc in boxCoords:
            if not possible(rr+dR, cc+dC, dR, dC, checked):
                return False
        return True

    r, c = robot
    printGrid()
    for m in movements:
        grid[r][c] = '.'
        dR, dC = signToMovement[m]
        nR, nC = r+dR, c+dC

        if grid[nR][nC] == '.':
            r, c = nR, nC
        elif grid[nR][nC] in '[]' and possible(nR, nC, dR, dC, set()):

            boxCoords = set()
            combined = combinedBox(nR, nC, dR, dC, boxCoords)
            newCoords = []
            for oR, oC in set(boxCoords):
                rr, cc = oR+dR, oC+dC
                newCoords.append((rr, cc, grid[oR][oC]))
                grid[oR][oC] = '.'

            for rr, cc, value in newCoords:
                grid[rr][cc] = value

            r, c = nR, nC
        grid[r][c] = '@'
        # printGrid()

    res = 0
    for r in range(M):
        for c in range(N):
            if grid[r][c] == '[':
                res += (r*100)+c

    printGrid()
    pr(res)


if __name__ == '__main__':
    main()
