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
    from collections import defaultdict
    neighbors = defaultdict(list)

    for line in lines:
        a, b = line.split('-')
        neighbors[a].append(b)
        neighbors[b].append(a)

    nodes = list(neighbors.keys())
    validSets = 0

    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            for k in range(j+1, len(nodes)):
                a, b, c = nodes[i], nodes[j], nodes[k]
                if c in neighbors[a] and c in neighbors[b] and b in neighbors[a]:
                    if any([x.startswith('t') for x in [a, b, c]]):
                        validSets += 1

    pr(validSets)


if __name__ == '__main__':
    main()
