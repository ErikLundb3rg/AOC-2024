import sys
import re
from collections import defaultdict, Counter
import pyperclip as pc

# Could not for the life of me figure out
# a programmatic solution.
# Used heavy help from https://www.reddit.com/user/lscddit/


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

    faulty = set()
    # print(wires)
    for a, operation, b, target in wires:
        # last output should be xor
        if target.startswith('z') and operation != 'XOR' and target != 'z45':
            faulty.add(target)
        if (
            operation == 'XOR' and
            set([a[0], b[0], target[0]]).isdisjoint(set(['x', 'y', 'z']))
        ):
            faulty.add(target)
        if operation == "AND" and 'x00' not in [a, b]:
            for oA, subOperation, oB, _ in wires:
                if (target == oA or target == oB) and subOperation != "OR":
                    faulty.add(target)
        if operation == "XOR":
            for oA, subOperation, oB, _ in wires:
                if (target == oA or target == oB) and subOperation == "OR":
                    faulty.add(target)

    pr(','.join(sorted(faulty)))


if __name__ == '__main__':
    main()
