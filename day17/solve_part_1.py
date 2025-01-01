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
    lines = getLines('example.in')
    A = int(lines[0].split(': ')[1])
    B = int(lines[1].split(': ')[1])
    C = int(lines[2].split(': ')[1])

    instructions = lines[4].split(': ')[1].split(',')
    instructions = [int(x) for x in instructions]

    def getCombo(x):
        if 0 <= x <= 3:
            return x
        if x == 4:
            return A
        if x == 5:
            return B
        if x == 6:
            return C
        assert "Error"

    i = 0
    res = []
    while i < len(instructions):
        opCode, operand = instructions[i], instructions[i+1]
        combo = getCombo(operand)

        jumped = False
        if opCode == 0:
            A = A // (2**combo)
        elif opCode == 1:
            B = B ^ operand
        elif opCode == 2:
            B = combo % 8
        elif opCode == 3:
            if A == 0:
                pass
            else:
                jumped = True
        elif opCode == 4:
            B = B ^ C
        elif opCode == 5:
            res.append(combo % 8)
        elif opCode == 6:
            B = A // (2**combo)
        elif opCode == 7:
            C = A // (2**combo)
        if jumped:
            i = operand
        else:
            i += 2

    pr(','.join([str(x) for x in res]))


if __name__ == '__main__':
    main()
