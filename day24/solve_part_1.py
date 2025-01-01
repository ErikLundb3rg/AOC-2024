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
    takingDefaults = True
    wireToValue = {}
    wires = []

    for line in lines:
        if not line:
            takingDefaults = False
            continue

        if takingDefaults:
            wire, value = line.split(': ')
            wireToValue[wire] = int(value)
        else:
            a, operation, b, _, target = line.split(' ')
            wires.append((a, operation, b, target))

    targetToOperation = {target: (a, operation, b)
                         for a, operation, b, target in wires}

    def evaluate(x):
        if x in wireToValue:
            return wireToValue[x]

        a, operation, b = targetToOperation[x]
        vA, vB = map(evaluate, [a, b])
        if operation == "XOR":
            return vA ^ vB
        elif operation == "OR":
            return vA | vB
        elif operation == "AND":
            return vA & vB

    zWires = sorted(
        [target for _, _, _, target in wires if target.startswith('z')], reverse=True)
    res = "".join([str(evaluate(z)) for z in zWires])
    print(res)
    pr(int(res, 2))


if __name__ == '__main__':
    main()
