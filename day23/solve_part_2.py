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
    neighbors = defaultdict(set)

    for line in lines:
        a, b = line.split('-')
        neighbors[a].add(b)
        neighbors[b].add(a)

    nodes = list(neighbors.keys())
    # check node against all neighbors,
    mx, mxRing = [0], [""]

    def dfs(node, previous, visited):
        key = (node, tuple(previous))
        if key in visited:
            return
        visited.add(key)

        for p in previous:
            if node not in neighbors[p]:
                return

        previous.append(node)
        if len(previous) > mx[0]:
            mx[0] = len(previous)
            mxRing[0] = ",".join(sorted(previous))

        for n in neighbors[node]:
            dfs(n, previous, visited)

    v = set()
    for baseNode in nodes:
        dfs(baseNode, [], v)
    print(mx)
    pr(mxRing[0])

    # pr(validSets)


if __name__ == '__main__':
    main()
